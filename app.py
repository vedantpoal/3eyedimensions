import streamlit as st
import torch
from diffusers import DiffusionPipeline
import imageio
from io import BytesIO
from PIL import Image

# Title of the app
st.title("Text-to-Video Generator")

# Load the model (only once when the app starts)
@st.cache_resource
def load_model():
    pipe = DiffusionPipeline.from_pretrained("cerspense/zeroscope_v2_576w", torch_dtype=torch.float16)
    pipe.enable_model_cpu_offload()
    pipe.unet.enable_forward_chunking(chunk_size=1, dim=1)
    pipe.enable_vae_slicing()
    return pipe

pipe = load_model()

# Text input for the prompt
prompt = st.text_input("Enter a text prompt for the video")

# If a prompt is entered, generate the video
if prompt:
    st.write("Generating video... please wait.")

    # Generate video frames
    video_frames = pipe(prompt, num_frames=24).frames[0]

    # Save video to in-memory buffer
    video_buffer = BytesIO()
    with imageio.get_writer(video_buffer, fps=10, format="mp4") as writer:
        for frame in video_frames:
            writer.append_data(frame)

    video_buffer.seek(0)

    # Display the video
    st.video(video_buffer, format="video/mp4")

    # Optional: Allow users to download the video
    st.download_button(label="Download Video", data=video_buffer, file_name="generated_video.mp4", mime="video/mp4")
