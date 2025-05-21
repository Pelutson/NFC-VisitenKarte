# NFC Token Web Access System

This project implements a simple NFC-based access control system using Python and Flask. When an NFC tag is scanned, a unique one-time token is generated and can be used to access a secure webpage.

## Features

- 🔐 **One-time token generation** on each NFC scan
- 🌐 **Web access interface** secured by tokens
- 📆 **Token expiration** (optional enhancement)
- ⚙️ **Built with Flask**, easily deployable

## How It Works

1. An NFC tag is scanned using a connected reader (e.g., USB or GPIO-based).
2. A backend Python script generates a unique token (e.g., UUID).
3. The token is stored (in memory or database) and optionally set to expire after a certain time.
4. A user can open a protected web page via a URL that includes the token (e.g., `https://yourdomain.com/access/<token>`).
5. The Flask server verifies the token and grants access if it's valid.

## Example Token Flow

1. NFC Scan → Token: `b3120f4e-4d26-11ee-be56-0242ac120002`
2. URL: `https://yourdomain.com/access/b3120f4e-4d26-11ee-be56-0242ac120002`
3. Server checks:
   - Is token valid?
   - Is token expired?
   - Was it already used?

## Possible Enhancements

- Store tokens in a database like SQLite or Redis
- Implement token usage logs
- Add expiration timestamps
- Add IP logging or rate limiting
- Use QR codes in addition to NFC

## Technologies

- Python 3
- Flask
- uuid / datetime
- Optional: nfcpy or GPIO libraries

