import streamlit as st
from keras import layers
from keras.layers import (Input, Add, Dense, Activation, ZeroPadding2D, BatchNormalization, 
                          Flatten, Conv2D, AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D,
                          Dropout)
from keras.models import Model, load_model
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from keras.initializers import glorot_uniform
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import load_img,img_to_array
from bing_image_downloader import downloader
from streamlit import caching

from unsplash_search import UnsplashSearch
unsplash = UnsplashSearch("C5OCp7HRCjNi9nr72kUXBpsY46mAPJizBcOrBEpA9EI")


st.write(""" # Music Genre Recognition 
App """)

st.write("Made By Bharath C S")
st.write("**This is a Web App to predict Genre of Music.**")
st.write("On the backend of this Web App a Convolutional Neural Network Model is used.The Model was trained on Mel Spectrogram of Music Files in the GTZAN Dataset.")
st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                width: 390px;
            }}
        </style>
    ''',
    unsafe_allow_html=True
)


@st.cache
def get_url(query):
  img = unsplash.search_photo(query)
  img_url = img['img']
  return img_url,img

def default_background():
  page_bg_img = '''
  <style>
  body {
  background-image: url("https://images.unsplash.com/photo-1421217336522-861978fdf33a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80");
  background-size: cover;
  }  
  </style>
  '''
  st.markdown(page_bg_img, unsafe_allow_html=True)

img_url,img = get_url("best landscape photos")


background = st.sidebar.radio("Do You Want Use Default Background or Change?",("Default Background","Change Background"))

def change_background():

  change = st.sidebar.button("Change Background of App")
  
  if(change):
    caching.clear_cache()
    img_url,img = get_url("best landscape photos")
    
    st.write("Photo By " + img['credits'] + " on Unsplash")
    page_bg_img = '''
    <style>
    body {
    background-image: url(''' +img_url+''');
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

if(background=="Default Background"): 
  default_background()
if(background=="Change Background"):
  page_bg_img = '''
  <style>
  body {
  background-image: url(''' +img_url+''');
  background-size: cover;
  }
  </style>
  '''
  st.markdown(page_bg_img, unsafe_allow_html=True)
  change_background()




st.set_option('deprecation.showfileUploaderEncoding', False)

file = st.sidebar.file_uploader("Please Upload Mp3 Audio File Here or Use Demo Of App Below using Preloaded Music",
type=["mp3"])

from PIL import Image
import librosa
import numpy as np
import librosa.display
from pydub import AudioSegment
import matplotlib.cm as cm
from matplotlib.colors import Normalize

class_labels = ['blues',
 'classical',
 'country',
 'disco',
 'hiphop',
 'metal',
 'pop',
 'reggae',
 'rock']

def GenreModel(input_shape = (288,432,4),classes=9):
 
 
  X_input = Input(input_shape)

  X = Conv2D(8,kernel_size=(3,3),strides=(1,1))(X_input)
  X = BatchNormalization(axis=3)(X)
  X = Activation('relu')(X)
  X = MaxPooling2D((2,2))(X)
  
  X = Conv2D(16,kernel_size=(3,3),strides = (1,1))(X)
  X = BatchNormalization(axis=3)(X)
  X = Activation('relu')(X)
  X = MaxPooling2D((2,2))(X)
  
  X = Conv2D(32,kernel_size=(3,3),strides = (1,1))(X)
  X = BatchNormalization(axis=3)(X)
  X = Activation('relu')(X)
  X = MaxPooling2D((2,2))(X)

  X = Conv2D(64,kernel_size=(3,3),strides=(1,1))(X)
  X = BatchNormalization(axis=-1)(X)
  X = Activation('relu')(X)
  X = MaxPooling2D((2,2))(X)

  X = Conv2D(128,kernel_size=(3,3),strides=(1,1))(X)
  X = BatchNormalization(axis=-1)(X)
  X = Activation('relu')(X)
  X = MaxPooling2D((2,2))(X)

  X = Conv2D(256,kernel_size=(3,3),strides=(1,1))(X)
  X = BatchNormalization(axis=-1)(X)
  X = Activation('relu')(X)
  X = MaxPooling2D((2,2))(X)

  
  X = Flatten()(X)

  #X = Dropout(rate=0.3)(X)

  #X = Dense(256,activation='relu')(X)

  #X = Dropout(rate=0.4)(X)

  X = Dense(classes, activation='softmax', name='fc' + str(classes), kernel_initializer = glorot_uniform(seed=9))(X)

  model = Model(inputs=X_input,outputs=X,name='GenreModel')

  return model

model = GenreModel(input_shape=(288,432,4),classes=9)
model.load_weights("genre.h5")


def convert_mp3_to_wav(music_file):
  sound = AudioSegment.from_mp3(music_file)
  sound.export("music_file.wav",format="wav")

def extract_relevant(wav_file,t1,t2):
  wav = AudioSegment.from_wav(wav_file)
  wav = wav[1000*t1:1000*t2]
  wav.export("extracted.wav",format='wav')

def create_melspectrogram(wav_file):
  y,sr = librosa.load(wav_file,duration=3)
  mels = librosa.feature.melspectrogram(y=y,sr=sr)
  
  fig = plt.Figure()
  canvas = FigureCanvas(fig)
  p = plt.imshow(librosa.power_to_db(mels,ref=np.max))
  plt.savefig('melspectrogram.png')


def download_image():
  filename = file.name
  filename = str.split(filename,"(")[0]
  downloader.download(filename + "Spotify", limit=1,  output_dir='/', adult_filter_off=True, force_replace=False, timeout=60)
  return filename

def download_image_demo(filename):
  downloader.download(filename + "Spotify", limit=1,  output_dir='/', adult_filter_off=True, force_replace=False, timeout=60)
  

def predict(image_data,model):

  #image = image_data.resize((288,432))
  image = img_to_array(image_data)

  image = np.reshape(image,(1,288,432,4))

  prediction = model.predict(image/255)

  prediction = prediction.reshape((9,)) 


  class_label = np.argmax(prediction)

  
  return class_label,prediction

def show_output(songname):
  convert_mp3_to_wav(songname + ".mp3")
  extract_relevant("music_file.wav",40,50)
  create_melspectrogram("extracted.wav") 
  image_data = load_img('melspectrogram.png',color_mode='rgba',target_size=(288,432))
  
  download_image_demo(songname)
  st.sidebar.write("The Song You have Choosen Is " +songname )
  st.sidebar.image(songname +"Spotify" + "/Image_1.jpg",use_column_width=True)
  st.sidebar.write("**Play the Song Below if you want!**")
  st.sidebar.audio(songname + ".mp3" ,"audio/mp3")  

  class_label,prediction = predict(image_data,model)

  st.write("## The Genre of Song is "+class_labels[class_label])

  spec_or_prob = st.sidebar.radio("Select one of Below",("Probability Distribution","Mel Spectrogram"))

  prediction = prediction.reshape((9,)) 
  
  color_data = [1,2,3,4,5,6,7,8,9]
  my_cmap = cm.get_cmap('jet')
  my_norm = Normalize(vmin=0, vmax=9)


  if(spec_or_prob =="Probability Distribution"):
    fig,ax= plt.subplots(figsize=(6,4.5))
    ax.bar(x=class_labels,height=prediction,
    color=my_cmap(my_norm(color_data)))
    plt.xticks(rotation=45)
    ax.set_title("Probability Distribution Of The Given Song Over Different Genres")
  
    plt.show()
    st.pyplot(fig)

  if(spec_or_prob=="Mel Spectrogram"):
    st.image("melspectrogram.png",use_column_width=True)

demo = st.sidebar.checkbox("Do You Want to check the App with Preloaded Music")

if(demo):
  
  song = st.sidebar.radio("Which Song you Want to check?",("Green Day-American Idiot","Taylor Swift-Love Story","Nirvana-Smells Like Teen Spirit","Muse-Plug In Baby"))

  if(song=="Green Day-American Idiot"):
    show_output("Green Day-American Idiot") 
  if(song=="Muse-Plug In Baby"):
    show_output("Muse-Plug In Baby")
  if(song=="Taylor Swift-Love Story"):
    show_output("Taylor Swift-Love Story")
  if(song=="Nirvana-Smells Like Teen Spirit"):
    show_output("Nirvana-Smells Like Teen Spirit")

if file is None:
  st.text("Please upload an mp3 file")
else:
  convert_mp3_to_wav(file)
  extract_relevant("music_file.wav",40,50)
  create_melspectrogram("extracted.wav") 
  image_data = load_img('melspectrogram.png',color_mode='rgba',target_size=(288,432))
  
  filename = download_image()
  st.sidebar.write("The Song You have Choosen Is " +filename )
  st.sidebar.image(filename +"Spotify" + "/Image_1.jpg",use_column_width=True)
  st.sidebar.write("**Play the Song Below if you want!**")
  st.sidebar.audio(file,"audio/mp3")
  
  class_label,prediction = predict(image_data,model)

  st.write("## The Genre of Song is "+class_labels[class_label])

  spec_or_prob = st.sidebar.radio("Select one of Below",("Probability Distribution","Mel Spectrogram"))

  prediction = prediction.reshape((9,)) 
  
  color_data = [1,2,3,4,5,6,7,8,9]
  my_cmap = cm.get_cmap('jet')
  my_norm = Normalize(vmin=0, vmax=9)


  if(spec_or_prob =="Probability Distribution"):
    fig,ax= plt.subplots(figsize=(6,4.5))
    ax.bar(x=class_labels,height=prediction,
    color=my_cmap(my_norm(color_data)))
    plt.xticks(rotation=45)
    ax.set_title("Probability Distribution Of The Given Song Over Different Genres")
  
    plt.show()
    st.pyplot(fig)

  if(spec_or_prob=="Mel Spectrogram"):
    st.image("melspectrogram.png",use_column_width=True)

  #st.text("Probability (0: Blues, 1: Classical, 2: Country,3: Disco,4: Hiphop,5: Metal,6: Pop,7: Reggae,8: Rock")
  #st.write(prediction)
