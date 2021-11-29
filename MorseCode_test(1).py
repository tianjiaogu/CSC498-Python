from MorseCode import *
# %% test Build_Character_Encoder
Character_Encoder = Build_Character_Encoder()
if Character_Encoder['a'] != '.-':
    print('something is wrong in Character_Encoder')
#%% test Build_Character_Decoder
Character_Decoder = Build_Character_Decoder()
if Character_Decoder['.-'] != 'a':
    print('something is wrong in Character_Decoder')
#%% test Word_Encoder
print('gin:', Word_Encoder('gin'))
print('zen', Word_Encoder('zen'))
print('gig', Word_Encoder('gig'))
print('msg', Word_Encoder('msg'))
#%%
Message1a = 'It is a good day to learn Python 3.6'
Message1b = 'it is a good day to learn python 3#6'
MessageInMorseCode = Message_Encoder(Message1b)
Message2 = Message_Decoder(MessageInMorseCode)
if Message1b != Message2:
     print('something is wrong in Message_Encoder or Message_Decoder')
#%% some examples to test Message_Encoder and Message_Decoder
#'Python is great'
#'.--. -.-- - .... --- -.,.. ...,--. .-. . .- -'     
#'Python is easy'
#'.--. -.-- - .... --- -.,.. ...,. .- ... -.--'
#'Python is powerful'
#'.--. -.-- - .... --- -.,.. ...,.--. --- .-- . .-. ..-. ..- .-..'     
#'We are using Python 3.6' or 'we are using python 3@6'
#'.-- .,.- .-. .,..- ... .. -. --.,.--. -.-- - .... --- -.,...-- .-.-.- -....'
#'the quick brown fox jumps over the lazy dog 0 1 2 3 4 5 6 7 8 9'
#'- .... .,--.- ..- .. -.-. -.-,-... .-. --- .-- -.,..-. --- -..-,.--- ..- -- .--. ...,--- ...- . .-.,- .... .,.-.. .- --.. -.--,-.. --- --.,-----,.----,..---,...--,....-,.....,-....,--...,---..,----.'     
#%% test sound
M1='It is a good day to learn Python 3.6'
C = Message_Encoder(M1)
M2 = Message_Decoder(C)
print(C)
print(M2)
Make_Sound(C)
#%% test email
Send_Message(play_sound = True)
