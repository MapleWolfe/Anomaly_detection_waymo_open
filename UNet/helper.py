"""
Description: Helper functions towards preprocessing the data


"""
import torch

def dice_loss(predicted, target):
    smooth = 1.0  # Smoothing factor to avoid division by zero
    intersection = torch.sum(predicted * target)
    union = torch.sum(predicted) + torch.sum(target)
    dice_coefficient = (2.0 * intersection + smooth) / (union + smooth)
    return 1.0 - dice_coefficient

def analyze_num_classes(seg_mask):
    num_classes = len(torch.unique(seg_mask))  # Count the unique grayscale values
    return num_classes

# Custom collate function to handle varying tensor sizes
def custom_collate(batch):
    # Get the maximum height and width in the current batch

    max_height = max([img.shape[0] for img, _ in batch])
    max_width = max([img.shape[1] for img, _ in batch])

    # Pad or resize images and labels to the maximum size
    padded_images = []
    padded_labels = []
    st_mask = []

    for img, label in batch:
        img_padded = pad(img, padding= (0, max_width - img.shape[1], 0, max_height - img.shape[0]), fill=255)
        label_padded = pad(label, padding = (0, max_width - label.shape[1], 0, max_height - label.shape[0]), fill=255)
        mask = (label_padded != 255).float()

        label_padded = label_padded.unsqueeze(0)
        img_padded = img_padded.unsqueeze(0)

        padded_images.append(img_padded)
        padded_labels.append(label_padded)

        st_mask.append(mask)

    # Stack the padded images and labels into a batch
    batch_images = torch.stack(padded_images, dim=0)
    batch_labels = torch.stack(padded_labels, dim=0)
    batch_mask = torch.stack(st_mask,dim=0)

    return batch_images, batch_labels, batch_mask
