import os
from PIL import Image

# Set path to image folder
folder = 'static'
output_path = os.path.join(folder, 'weather_combined_dashboard.png')

# Cities in order
cities = [
    'Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Chennai',
    'Coimbatore', 'Agra', 'Pune', 'Kochi', 'Jaipur'
]

# Load and verify image pairs
image_pairs = []
for i, city in enumerate(cities, start=1):
    bar = os.path.join(folder, f'dashboard_{i}_{city}.png')
    forecast = os.path.join(folder, f'forecast_{i}_{city}.png')
    if os.path.exists(bar) and os.path.exists(forecast):
        image_pairs.append((bar, forecast))
    else:
        print(f'❌ Missing charts for {city}')

# Resize settings
width, height = 400, 300

# Prepare resized images
resized_images = []
for bar_path, forecast_path in image_pairs:
    bar_img = Image.open(bar_path).resize((width, height))
    forecast_img = Image.open(forecast_path).resize((width, height))
    resized_images.extend([bar_img, forecast_img])

# New layout: 2 chart rows per city × 5 cities per row
charts_per_row = 5
cities_per_row = 5
total_rows = 4  # 2 chart rows × 2 rows of cities

# Final image size
final_width = width * cities_per_row
final_height = height * total_rows
combined = Image.new('RGB', (final_width, final_height), color='white')

# Paste images row by row
for idx, img in enumerate(resized_images):
    col = (idx // 2) % charts_per_row
    city_row = (idx // 2) // charts_per_row
    chart_row = idx % 2  # 0 = bar chart, 1 = forecast

    x = col * width
    y = (city_row * 2 + chart_row) * height
    combined.paste(img, (x, y))

# Save result
combined.save(output_path)
print(f"\n✅ Combined dashboard saved as: {output_path}")

