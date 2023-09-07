import albumentations as A
import cv2
from glob import glob


transform = A.Compose(
    [
        A.RandomCrop(width=640, height=640),
        A.HorizontalFlip(p=1)
    ],
    bbox_params=A.BboxParams(format='yolo')
)

pathesImages, pathesLabels = glob('sber/train/images/*'), glob('sber/train/labels/*')
for pthImg, pthLabel in zip(pathesImages, pathesLabels):
    image = cv2.imread(pthImg)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pthWrite = pthLabel[pthLabel.find('labels') + 7:]
    dataFile = []
    with open(pthLabel, 'r', encoding='utf-8') as file:
        dataFile = file.readlines()
    # if len(dataFile) > 0:
    with open('labels/HorizontalFlip' + pthWrite, 'w', encoding='utf-8') as writeAnot:
        agumin = [list(map(lambda j: float(j), x.strip().split()[1:])) + ['0'] for x in dataFile]

        transformed = transform(image=image, bboxes=agumin, class_labels=['0'])
        transformed_image = transformed['image']
        transformed_bboxes = transformed['bboxes']

        # writeAnot.writelines(data)
        data = []
        for i in transformed_bboxes:
            data.append(str(i[-1]) + ' ' + ' '.join(map(lambda x: str(x), i[:-1])) + '\n')
        writeAnot.writelines(data)
        cv2.imwrite('images/HorizontalFlip' + pthImg[pthImg.find('images') + 7:], transformed_image)
print('one Done')

transform = A.Compose(
    [
        A.RandomCrop(width=640, height=640)
    ],
    bbox_params=A.BboxParams(format='yolo')
)
for pthImg, pthLabel in zip(pathesImages, pathesLabels):
    image = cv2.imread(pthImg)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pthWrite = pthLabel[pthLabel.find('labels') + 7:]
    dataFile = []
    with open(pthLabel, 'r', encoding='utf-8') as file:
        dataFile = file.readlines()
    with open('labels/' + pthWrite, 'w', encoding='utf-8') as writeAnot:
        agumin = [list(map(lambda j: float(j), x.strip().split()[1:])) + ['0'] for x in dataFile]
        transformed = transform(image=image, bboxes=agumin, class_labels=['0'])
        transformed_image = transformed['image']
        transformed_bboxes = transformed['bboxes']

        # writeAnot.writelines(data)
        data = []
        for i in transformed_bboxes:
            data.append(str(i[-1]) + ' ' + ' '.join(map(lambda x: str(x), i[:-1])) + '\n')
        writeAnot.writelines(data)
        cv2.imwrite('images/' + pthImg[pthImg.find('images') + 7:], image)
print('two Done')

print('all Done')