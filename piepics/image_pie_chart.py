import os
import matplotlib.pyplot as plt

# --- Change this to your folder path ---
image_folder = r"C:\Users\Ananya\OneDrive\Pictures\piepics"

image_names = []
image_sizes = []

# Read images and get sizes
for file in os.listdir(image_folder):
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        file_path = os.path.join(image_folder, file)
        size_mb = os.path.getsize(file_path) / (1024 * 1024)  # size in MB
        
        image_names.append(file)
        image_sizes.append(size_mb)

# Donut pie chart
plt.figure(figsize=(10, 10))
wedges, texts, autotexts = plt.pie(
    image_sizes,
    labels=image_names,        # show image names
    autopct=lambda pct: f'{pct:.1f}%\n({pct/100*sum(image_sizes):.2f} MB)',
    startangle=90,
    pctdistance=0.75
)

# Donut center
centre_circle = plt.Circle((0, 0), 0.50, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')
plt.tight_layout()
plt.show()
