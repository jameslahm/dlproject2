import face_alignment
from skimage import io

# cuda for CUDA
fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, device='cpu')

input = io.imread('data/00001.jpg')
preds = fa.get_landmarks(input)