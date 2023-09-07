<h1 align="center">Hackathon challenge ML Hackathon: Utashud's wild life!</h1>

<h2 align="center">Hackathon Challenge: Seagulls</h2>

> Utashud Island, part of the South Kamchatka Federal Reserve, lies 4 kilometers from the Pacific coast of Kamchatka in Vestnik Bay. Sea otters, anthurs, spotted seals, about 50,000 birds of ten different species live on it, including a colony of 10,000 hatchet pairs. At the hackathon, we are interested in two inhabitants of the island - spotted seal and techno-ocean gull, which are monitored through camera traps in the summer season.

> On Utashuda there is a reproductive rookery of spotted seals and one of the largest settlements of the slaty-backed gull in Kamchatka (4 thousand pairs). For 1 season of observing these animals, more than 1800 photographs of various quality can be accumulated. Through these photographs, inspectors assess the welfare and abundance of animals.

> Develop an algorithm to count seagulls that are larger than 5x5 pixels in a photograph and help the researchers.

<h4 align="justify">Task metric - (1-RMSE). You can read about how it is calculated in the task baseline.</h4>

<h2 align="center">Decision progress</h2>

<h3 align="center">Dataset extension</h3>

<h4 align="justify">The initial dataset consisted of 500 photos for the training sample, and 99 photos for the validation sample. I decided to expand the training dataset using the albumentations framework, which resulted in 1198 images for training.</h4>

<h3 align="center">Choose model</h3>

<h4 align="justify">For training, I decided to take the yolov5x model with an image size of 640 * 640, the maximum possible batch size (and this is -1 which automatically fills free space in RAM), 128 epochs.</h4>

## **Submition score and place that turned out during the hackathon**
### **Public  -1.4052026941611389**
### **Private  -1.126590712784548**
### **I took 5th place in the top 10**
