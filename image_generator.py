# Image Generator Script

# Import the replicate library
import replicate

# Generate an image using the specified model and input
output = replicate.run(
  "black-forest-labs/flux-schnell",
  input={"prompt": "an iguana on the beach, pointillism"}
)

# Save the generated image
with open('output.png', 'wb') as f:
    f.write(output[0].read())

# Print confirmation message
print(f"Image saved as output.png")