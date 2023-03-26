#import dorpbox library
import dropbox

# defining a class to interact with Dropbox
class dropbox_storage:
    
    # defining the constructor to initialize the Dropbox access token
    def __init__(self, access_token):
         # saving the access token as a class variable
        self.at=access_token 

    # defining the  method to upload a file to Dropbox
    def uploadFile(self, file_from, file_to):
        # opening the file to be uploaded in binary mode
        f = open(file_from, 'rb')  
        # creating the  Dropbox object using the access token
        dbx = dropbox.Dropbox(self.at)  

        # checking to see if the file locations are provided
        if file_from != '' and file_to != '':
            # uploading the file to Dropbox
            dbx.files_upload(file_from, file_to)
            # printing a success message
            print("Your file has been successfully uploaded") 

        else:
            # printing the error message if file locations are not provided
            print("File location and file storage location are needed to proceed")  
# defining the main function to interact with the user
def main():
    # printing a welcome message
    print("Welcome to Dropbox cloud storage services")  
    print(" ")
    
    # getting the Dropbox access token from the user
    authentication_token = input("Please enter your Dropbox access token: ")
     # creating the  cloud_storage object using the access token
    user = dropbox_storage(authentication_token) 
    print("")

    # looping until the user chooses to exit
    while True:
        # asking the user if they want to upload a file to Dropbox
        Ques = input("Would you like to upload a file to Dropbox? (y/n)").lower()
        print("")

        if Ques == 'y':  # if the user wants to upload a file
            # getting the file name and the Dropbox folder to upload the file to
            ff = input("Please enter the file name you would like to upload: ")
            ft = input("Please enter the folder where you would like to upload your file on Dropbox: ")
            # constructing the full Dropbox file path
            ft = '/' + ft + '/' + ff  
            
            print(" ")
             # uploading the file to Dropbox
            user.uploadFile(ff, ft)  

        elif Ques == 'n':  # if the user does not want to upload a file
             # print a goodbye message
            print("Thank you for using our program")  
            break  # exit the loop and end the program
        # if the user enters an invalid option
        else: 
            print("Please answer with either y/n")  # print an error message
