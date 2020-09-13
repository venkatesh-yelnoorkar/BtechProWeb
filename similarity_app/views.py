from django.shortcuts import render
from .forms import TitleForm, AbstractForm

# Create your views here.
def index(request):
    return render(request, "similarity_app/index.html")
    pass

def title(request):
    if request.method == "POST":
        print("************")
        form = TitleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            # simialr_list will contain the list of sililar papers
            # format of similar list is as follows :
            similar_list = [
                                {
                                    "id":"xzyid", 
                                    "title":"Pixel-level Encoding and Depth Layering for Instance-level Semantic Labeling", 
                                    "abstract":"xyzabs", 
                                    "similarity":"xyzsim",
                                },
                                
                                {
                                    "id":"abc", 
                                    "title":"abc", 
                                    "abstract":"abc", 
                                    "similarity":"abc",
                                },
                            ]
            # similar_list = get_similar(data = title, title = True, n = 5)
            context = {
                "data":title,
                "similar_list":similar_list,
                "type":"Title",

            }
            return render(request, "similarity_app/sim_list.html", context)


        
    else:
        form = TitleForm()
        context = {
            "form":form,
            "type":"Title",
        }
        return render(request, "similarity_app/data_input.html", context)

def abstract(request):
    if request.method == "POST":
        print("************")
        form = AbstractForm(request.POST)
        if form.is_valid():
            abstract = form.cleaned_data["abstract"]
            # simialr_list will contain the list of sililar papers
            # format of similar list is as follows :
            similar_list = [
                                {
                                    "id":"url", 
                                    "title":"Title", 
                                    "abstract":"Abstract", 
                                    "similarity":"Cosine distance",
                                },

                                {
                                    "id":"http://arxiv.org/abs/1604.05096v2", 
                                    "title":"Pixel-level Encoding and Depth Layering for Instance-level Semantic Labeling", 
                                    "abstract":"Recent approaches for instance-aware semantic labeling have augmentedconvolutional neural networks (CNNs) with complex multi-task architectures orcomputationally expensive graphical models. We present a method that leveragesa fully convolutional network (FCN) to predict semantic labels, depth and aninstance-based encoding using each pixel's direction towards its correspondinginstance center. Subsequently, we apply low-level computer vision techniques togenerate state-of-the-art instance segmentation on the street scene datasetsKITTI and Cityscapes. Our approach outperforms existing works by a large marginand can additionally predict absolute distances of individual instances from amonocular image as well as a pixel-level semantic labeling.", 
                                    "similarity":0.258529365,
                                },
                                
                                {
                                    "id":"http://arxiv.org/abs/1608.01441v1", 
                                    "title":"Improving Multi-label Learning with Missing Labels by Structured Semantic Correlations", 
                                    "abstract":"Multi-label learning has attracted significant interests in computer visionrecently, finding applications in many vision tasks such as multiple objectrecognition and automatic image annotation. Associating multiple labels to acomplex image is very difficult, not only due to the intricacy of describingthe image, but also because of the incompleteness nature of the observedlabels. Existing works on the problem either ignore the label-label andinstance-instance correlations or just assume these correlations are linear andunstructured. Considering that semantic correlations between images areactually structured, in this paper we propose to incorporate structuredsemantic correlations to solve the missing label problem of multi-labellearning. Specifically, we project images to the semantic space with aneffective semantic descriptor. A semantic graph is then constructed on theseimages to capture the structured correlations between them. We utilize thesemantic graph Laplacian as a smooth term in the multi-label learningformulation to incorporate the structured semantic correlations. Experimentalresults demonstrate the effectiveness of the proposed semantic descriptor andthe usefulness of incorporating the structured semantic correlations. Weachieve better results than state-of-the-art multi-label learning methods onfour benchmark datasets.", 
                                    "similarity":0.291086793,
                                },
                                {
                                    "id":"http://arxiv.org/abs/1511.04242v1", 
                                    "title":"Volume-based Semantic Labeling with Signed Distance Functions", 
                                    "abstract":"Research works on the two topics of Semantic Segmentation and SLAM(Simultaneous Localization and Mapping) have been following separate tracks.Here, we link them quite tightly by delineating a category label fusiontechnique that allows for embedding semantic information into the dense mapcreated by a volume-based SLAM algorithm such as KinectFusion. Accordingly, ourapproach is the first to provide a semantically labeled dense reconstruction ofthe environment from a stream of RGB-D images. We validate our proposal using apublicly available semantically annotated RGB-D dataset and a) employing groundtruth labels, b) corrupting such annotations with synthetic noise, c) deployinga state of the art semantic segmentation algorithm based on ConvolutionalNeural Networks.", 
                                    "similarity":0.301721871,
                                },
                            ]
            # similar_list = get_similar(data = title, title = True, n = 5)
            context = {
                "data":abstract,
                "similar_list":similar_list,
                "type":"Abstract",

            }
            return render(request, "similarity_app/sim_list.html", context)


        
    else:
        form = AbstractForm()
        context = {
            "form":form,
            "type":"Abstract",
        }
        return render(request, "similarity_app/data_input.html", context)
