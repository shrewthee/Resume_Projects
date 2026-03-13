import requests

def onView():
    # api url
    url = "https://api.artic.edu/api/v1/artworks/search"
    
    # ask the user for an artwork title
    artTitle = input("Enter the title of an artwork: ")
    
    # define parameters
    params = {
        "q": artTitle,  # look for title
        "fields": "title,is_on_view,artist_display",  # get title and information about the artwork
        "limit": 1  # only get one piece of artwork as a response
    }
    
    try:
        #get request
        response = requests.get(url, params=params)
        response.raise_for_status() 
        
        # parse
        data = response.json()
        artworks = data.get("data", []) 
        
        if not artworks:
            print(f"No artworks found with the title '{artTitle}'.")
        else:
            artwork = artworks[0]
            title = artwork.get("title", "Unknown Title")
            isOnView = artwork.get("isOnView", False)
            artist = artwork.get("artist_display", "Unknown Artist")
            
            if isOnView:
                print(f"The artwork '{title}' by {artist} is currently on view.")
            else:
                print(f"The artwork '{title}' is not on view.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

#run
if __name__ == "__main__":
    onView()
