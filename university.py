# List of university dictionaries
universities = [
    {"id": 1, "name": "University of the Philippines", "location": "Quezon City", "established_year": 1908, "type": "Public", "website": "www.up.edu.ph"},
    {"id": 2, "name": "Ateneo de Manila University", "location": "Quezon City", "established_year": 1859, "type": "Private", "website": "www.ateneo.edu"},
    {"id": 3, "name": "De La Salle University", "location": "Manila", "established_year": 1911, "type": "Private", "website": "www.dlsu.edu.ph"},
    {"id": 4, "name": "University of Santo Tomas", "location": "Manila", "established_year": 1611, "type": "Private", "website": "www.ust.edu.ph"},
    {"id": 5, "name": "Polytechnic University of the Philippines", "location": "Manila", "established_year": 1904, "type": "Public", "website": "www.pup.edu.ph"}
]

# Print university data
print("University Data:")
for university in universities:
    print(f"ID: {university['id']}, Name: {university['name']}, Location: {university['location']}, Established Year: {university['established_year']}, Type: {university['type']}, Website: {university['website']}")
