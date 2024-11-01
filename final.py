from speechTOtext import speech_to_csv
from truncateDirectory  import deleteFiles
from customTemplating import create_personalized_invitation_simple

image_path = "template.png"
csv_file = "words.csv"
output_dir = "personalized_invitations"
font_path = "Alice-Regular.ttf"
font_size = 80
font_color = "20520c"
y_coordinate = 548  # Keep Y fixed

# delete old files
deleteFiles(output_dir)

# Speech to Csv
speech_to_csv(csv_file)

# Custom Invitation
create_personalized_invitation_simple(image_path, csv_file, output_dir, font_path, font_size, font_color, y_coordinate)