import face_alignment
from skimage import io

# cuda for CUDA
fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, device='cuda')

## 人脸关键点标记
def getLandMark(file):
    input = io.imread(file)
    preds = fa.get_landmarks(input)

