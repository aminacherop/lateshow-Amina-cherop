#lateshow-Amina-cherop

A simple Flask API to manage **Episodes**, **Guests**, and their **Appearances**.

## Tech Stack
- Flask + SQLAlchemy
- SQLite (default)
- Flask-Migrate
- SQLAlchemy-Serializer

## Models
- **Episode**: `id`, `date`, `number`
- **Guest**: `id`, `name`, `occupation`
- **Appearance**: `id`, `rating`, `guest_id`, `episode_id`

Relationships:
- An Episode has many Guests through Appearances
- A Guest has many Episodes through Appearances

## Validations
- `rating` must be between `1` and `5`
- Appearance must belong to valid `guest_id` and `episode_id`

## API Endpoints

| Method | Route               | Description                     |
|--------|---------------------|---------------------------------|
| GET    | `/episodes`         | List all episodes               |
| GET    | `/episodes/<id>`    | Show episode + appearances      |
| GET    | `/guests`           | List all guests                 |
| POST   | `/appearances`      | Create new appearance           |

##Setup

```bash
git clone <https://github.com/aminacherop/lateshow-Amina-cherop>

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db upgrade
python seed.py
flask run

Testing
Use Postman to test endpoints. A Postman collection is provided.

Cascading Deletes
Deleting a Guest or Episode automatically deletes associated Appearances.

License
This project is open-source and available under the MIT License.

