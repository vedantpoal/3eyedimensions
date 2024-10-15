# Text-to-Video Generator

Welcome to the **Text-to-Video Generator**! This project allows users to generate videos from text prompts using state-of-the-art machine learning models. It is built on the **Diffusers** library from Hugging Face and is deployed as a Streamlit application on Hugging Face Spaces.

## Live Demo

You can try the application live at the following link:

[Text-to-Video Generator on Hugging Face Spaces](https://huggingface.co/spaces/vedantpoal/Vedant_text_to_video)

## Overview

The Text-to-Video Generator takes user-defined text prompts and generates corresponding videos. By leveraging advanced diffusion models, the application provides a seamless experience for users to create videos based on their imagination.

## Features

- Input any text prompt to generate a video.
- View the generated video directly in the application.
- Download the video for offline use.

## How to Use

1. **Access the Application**:
   - Visit the [Text-to-Video Generator on Hugging Face Spaces](https://huggingface.co/spaces/vedantpoal/Vedant_text_to_video).

2. **Input a Text Prompt**:
   - Enter your desired prompt in the input field (e.g., "A cat dancing on the beach").

3. **Generate the Video**:
   - Click the "Generate Video" button to start the process. Wait for a few moments as the video is generated.

4. **View and Download**:
   - Once the video is ready, it will be displayed on the page, and you can download it using the provided link.

## Technical Details

This application uses the **Zeroscope V2** model for generating video frames based on text prompts. The model has been fine-tuned to produce visually coherent videos for a variety of prompts.

### Requirements

This project was developed using the following libraries:

- Streamlit
- Hugging Face Diffusers
- Transformers
- PyTorch
- Imageio

These dependencies are automatically managed by Hugging Face Spaces, so you don't need to install them manually.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Hugging Face](https://huggingface.co/)
- [Diffusers](https://github.com/huggingface/diffusers)
- [Streamlit](https://streamlit.io/)

