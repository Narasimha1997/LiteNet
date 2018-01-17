# LiteNet
A simple CNN architecture to solve simple computer vision problems.


<h4>Architecture details </h4>
<p>The model is simple in nature and is built keeping speed and efficiency in mind. It contains a single CNN layer, connected to single dense layer with 512 units. It also contains a dropout layer to avoid Overfitting, in the same a single MaxPooling2D layer is used to obtain Max values from output of CNN layer. This model can be extended for multiple classes, just by increasig the number of output neurons, and by adding new dense layers to improve learnability. </p>

<h5>Basic idea behind LiteNets </h5>
<p>We often use complex pretrained networks like AlexNet, VGG and Inception for simple Computer Vision problems and fine tune them. Using large networks takes large amount of training time, and requires huge memory space to run. The memory space and training time depends on number of traniable parameters.</p>  

<p>   But the above method is suitable for computer vision problems which are complex in nature, most of the computer vision problems we encounter doesn't actually require large deep networks. </p>
