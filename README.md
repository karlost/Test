# Test

## Image Generator

This project includes a simple image generator script that uses the `replicate` library to generate images based on a given prompt. The script saves the generated image as `output.png`.

### How to Run

1. **Install the `replicate` library**:
   ```bash
   pip install replicate
   ```

2. **Set the Replicate API Token**:
   ```bash
   export REPLICATE_API_TOKEN=your_replicate_api_token
   ```

3. **Run the script**:
   ```bash
   python image_generator.py
   ```

This will generate an image based on the prompt "an iguana on the beach, pointillism" and save it as `output.png`.