import os
import shutil
import random

def split_dataset(input_images_folder, input_labels_folder, output_folder, train_percent=0.85, val_percent=0.10, test_percent=0.05):
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'images', 'train'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'images', 'val'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'images', 'test'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'labels', 'train'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'labels', 'val'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'labels', 'test'), exist_ok=True)

    image_files = [f for f in os.listdir(input_images_folder) if f.endswith('.jpg')]
    label_files = [f for f in os.listdir(input_labels_folder) if f.endswith('.txt')]

    random.shuffle(image_files)

    total_files = len(image_files)
    train_count = int(total_files * train_percent)
    val_count = int(total_files * val_percent)
    test_count = total_files - train_count - val_count

    train_images = image_files[:train_count]
    val_images = image_files[train_count:train_count + val_count]
    test_images = image_files[train_count + val_count:]

    for img_file in train_images:
        shutil.copy(os.path.join(input_images_folder, img_file), os.path.join(output_folder, 'images', 'train', img_file))
        label_file = os.path.splitext(img_file)[0] + '.txt'
        shutil.copy(os.path.join(input_labels_folder, label_file), os.path.join(output_folder, 'labels', 'train', label_file))

    for img_file in val_images:
        shutil.copy(os.path.join(input_images_folder, img_file), os.path.join(output_folder, 'images', 'val', img_file))
        label_file = os.path.splitext(img_file)[0] + '.txt'
        shutil.copy(os.path.join(input_labels_folder, label_file), os.path.join(output_folder, 'labels', 'val', label_file))

    for img_file in test_images:
        shutil.copy(os.path.join(input_images_folder, img_file), os.path.join(output_folder, 'images', 'test', img_file))
        label_file = os.path.splitext(img_file)[0] + '.txt'
        shutil.copy(os.path.join(input_labels_folder, label_file), os.path.join(output_folder, 'labels', 'test', label_file))

def main():
    input_images_folder = '/home/pc_5053/TEKNOFEST_UYZ/DATASET/images'
    input_labels_folder = '/home/pc_5053/TEKNOFEST_UYZ/YOLO_OUTPUT'
    output_folder = '/home/pc_5053/TEKNOFEST_UYZ/train_dataset_12.01.2024'

    split_dataset(input_images_folder, input_labels_folder, output_folder)

if __name__ == "__main__":
    main()