import json
from pathlib import Path
import sys

def convert_to_coco(path_of_folder):
    converted_dataset = dict()
    converted_dataset['info'] = {'year':2021,
                                'version': 1,
                                'description': "COCO annotations from kvasir-seg dataset "
                                }

    converted_dataset['categories'] = [ 
        {'id':0,'name':'polyp'}
        ]


    path = Path(path_of_folder)
    json_string= (path / 'kavsir_bboxes.json').read_text()

    dataset=json.loads(json_string)

    images = [ ]
    annotations = [ ]
    counter_image = 0
    counter_annotations = 0

    for item in dataset:
        value=dataset[item]

        image = {
                "id": counter_image,
                "file_name":item+".jpg",
                "height": value['height'],
                "width":value['width']
                }

        images.append(image)

        for annotation in value['bbox']:
            label= annotation['label']
            xmin = annotation['xmin']
            xmax = annotation['xmax']
            ymin = annotation['ymin']
            ymax = annotation['ymax']

            if xmax > value['width'] or ymax > value['height']:
                print('error in picture'+ counter_image) 

            width = xmax - xmin + 1
            height = ymax - ymin + 1
            area = width * height


            if label != 'polyp':
                raise 'invalid label'


            annotations.append({
                'id': counter_annotations,
                'image_id': counter_image,
                'category_id': 0,
                'area': area,
                'bbox': [xmin, ymin, width, height],
                'iscrowd': 0
            })
            counter_annotations = counter_annotations + 1
        counter_image = counter_image + 1

    converted_dataset['images'] = images
    converted_dataset['annotations'] = annotations

    (path/'kvasir-coco.json').write_text(json.dumps(converted_dataset))
    print('Done')

if __name__ == '__main__':
    if len(sys.argv)>1:
        convert_to_coco(sys.argv[1])
    else:
        convert_to_coco('/run/media/amir/hard/Dataset/Kvasir-SEG/')