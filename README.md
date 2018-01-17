# LiteNet
A simple CNN architecture to solve simple computer vision problems.


<h4>Architecture details </h4>
<p>The model is simple in nature and is built keeping speed and efficiency in mind. It contains a single CNN layer, connected to single dense layer with 512 units. It also contains a dropout layer to avoid Overfitting, in the same a single MaxPooling2D layer is used to obtain Max values from output of CNN layer. This model can be extended for multiple classes, just by increasig the number of output neurons, and by adding new dense layers to improve learnability. </p>

<h5>Basic idea behind LiteNets </h5>
<p>We often use complex pretrained networks like AlexNet, VGG and Inception for simple Computer Vision problems and fine tune them. Using large networks takes large amount of training time, and requires huge memory space to run. The memory space and training time depends on number of traniable parameters.</p>  

<p>   But the above method is suitable for computer vision problems which are complex in nature, most of the computer vision problems we encounter doesn't actually require large deep networks. For example, if we take MNIST handwritten digits recognition problem, the goal is to classify digits which are different from each other, such kind of vision problems does't require complex neural networks like Inception or VGG. We can construct simple single layer CNNs to solve such problems.</p>

<p> Neural netwoks for computer vision are usually built by using CNN along with dense network, CNN takes image matrix as input and produces a feature matrix. This feature matrix is given to Dense layers, the task of dense layer is to map the feature matrix to respective output label by activating the respective output neuron.</p>

<p>Dense layers are very good at learning patterns from feature matrix, if vison problem is simple and involves classification of classes which are distinct from one another, the feature matrix will be very unique for each of the classes, therefore single CNN layer is enough to produce feature matrices for unique classes, but same doesn't hold true if there are large number of classes which are similar to one another. The idea of LiteNet is to concentrate more on Dense layers rather than stacking up more CNN layers. The dense layers can easily be stacked up with minimum performance cost. These dense layers can be used to learn feature matrices which are unique. </p>

<h4>When to use LiteNet</p>
<p>There are few consequences where LiteNets can be used:</p>
<p> 1. Simple vision problems involving distinct recognition tasks where classes are distinct from each other, for example it can be used for a vision problem involving classification of Apple and Banana, which are distinct from each other.</p>
<p> 2. Simple learning models used in hobby projects and small scale tasks.</p>
<p> 3. Minimum number of output classes, (Ex: 4-5 classes)</p>

<h4>Advantages</h4>
<p>1. Simple</p>
<p>2. Less training time</p>
<p>3. Easily embedded into applications and servers</p>
<p>4. Solves simple computer vision problems</p>

<h4>Limitations</h4>
<p>1. Overfitting</p>
<p>2. Can be used only if dataset contains classes which are distinct and clearly distinguishable from each other</p>
<p>3. Minimum number of output classes</p>


<p>This repo contains a LiteNet trained on Flowers dataset downloaded from Tensorflow website</p>
<p>The model is built using Keras API</p>

