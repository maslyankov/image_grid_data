import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker
from os import path

try:
    from PIL import Image
except ImportError:
    import Image
from PIL.ExifTags import TAGS


def get_image_data(image):
    # read the image data using PIL
    img_obj = Image.open(image)

    # extract EXIF data
    exifdata = img_obj.getexif()

    # iterating over all EXIF data fields
    out_data = dict()
    out_data['filename'] = image

    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes
        if isinstance(data, bytes):
            data = data.decode()

        out_data[tag] = data
        print(f"{tag:25}: {data}")

    return out_data


def add_grid_to_image(image):
    img_dir = path.dirname(image)
    img_filename = path.basename(image)

    img_data = get_image_data(image)
    # img_data['ImageLength']
    # img_data['ImageWidth']

    img_filename_split = img_filename.split('.')
    img_name = img_filename_split[0]
    img_ext = img_filename_split[1]

    # Open image file
    image = Image.open(image)

    plt.figure(figsize=(6, 3.2))
    plt.subplots_adjust(top=0.9, bottom=0.1)
    img = np.random.rand(350, 350)

    plt.imshow(image, 'gray', vmin=-1, vmax=1)

    my_dpi = 100.
    linewidth = 0.72

    x_spacing = img_data['ImageLength']
    y_spacing = img_data['ImageWidth']

    # 17x13
    plt.minorticks_on()
    plt.gca().xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(100))
    plt.gca().yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(330))
    plt.grid(which="both", linewidth=linewidth, color="k", drawstyle='steps', clip_on=False, zorder=0.1, alpha=.6)
    plt.tick_params(which="both", length=0)

    plt.show()

    # my_dpi = 300.
    #
    # # Set up figure
    # fig = plt.figure(figsize=(float(image.size[0]) / my_dpi, float(image.size[1]) / my_dpi), dpi=my_dpi)
    # ax = fig.add_subplot(111)
    #
    # # Remove whitespace from around the image
    # fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    #
    # # Set the gridding interval: here we use the major tick interval
    # myInterval0 = 100.
    # myInterval1 = 200.
    # loc0 = plticker.MultipleLocator(base=myInterval0)
    # loc1 = plticker.MultipleLocator(base=myInterval1)
    # ax.xaxis.set_major_locator(loc0)
    # ax.yaxis.set_major_locator(loc1)
    #
    # # Add the grid
    # ax.grid(which='major', axis='both', linestyle='-')
    #
    # # Add the image
    # ax.imshow(image)
    #
    # # Find number of gridsquares in x and y direction
    # # nx = abs(int(float(ax.get_xlim()[1] - ax.get_xlim()[0]) / float(myInterval)))
    # # ny = abs(int(float(ax.get_ylim()[1] - ax.get_ylim()[0]) / float(myInterval)))
    # # 17x13
    # nx = 17
    # ny = 13
    #
    # # Add some labels to the gridsquares
    # for j in range(ny):
    #     y = myInterval0 / 2 + j * myInterval0
    #     for i in range(nx):
    #         x = myInterval1 / 2. + float(i) * myInterval1
    #         ax.text(x, y, '{:d}'.format(i + j * nx), color='w', ha='center', va='center')

    # Save the figure
    new_img_name = f"{img_name}_gridded.{img_ext}"
    new_img_path = path.join(img_dir, new_img_name)

    plt.savefig(new_img_path, dpi=my_dpi)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add_grid_to_image("data/snapshot_294_499890577099.jpg")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
