# Guide: How to Obtain a Spotify Refresh Token

A Spotify refresh token allows you to access the Spotify API on behalf of an authenticated user without requiring manual authorization each time.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3 installed on your machine.
- A Spotify account (a premium account is **not** required to obtain a refresh token).

## Step 1: Set Up a Spotify Developer Account

1. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in with your Spotify account credentials.
2. Click on **Create an App** and fill in the necessary details, such as the app name and description.
3. After creating your app, you will be redirected to the app dashboard. Note down the **Client ID** and **Client Secret**; you will need these later.
4. In the app dashboard, click on **Edit Settings** and add a redirect URI. Set it to **http://localhost:4321** for this example.
5. Save your changes.

## Step 2: Set Up a Python Virtual Environment (Optional but Recommended)

Setting up a virtual environment helps isolate project dependencies and avoid conflicts with other Python projects. Follow these steps to set up a Python virtual environment:

1. Open a command prompt or terminal.
2. Navigate to the directory where you want to create the virtual environment.
3. Run the following command to create a new virtual environment named "spotify-env":

   - For Windows:
     ```powershell
     python -m venv spotify-env
     ```
   - For macOS/Linux:
     ```bash
     python3 -m venv spotify-env
     ```

4. Activate the virtual environment:

   - For Windows:
     ```powershell
     .\spotify-env\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source spotify-env/bin/activate
     ```

   You should see the virtual environment name (e.g., "spotify-env") in your command prompt or terminal.

## Step 3: Clone the Repository

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/arnvgh/get-spotify-refresh-token
   ```
2. Navigate to the project directory:
   ```bash
   cd get-spotify-refresh-token
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Step 4: Create a `.env` File

1. Create a `.env` file in the project directory (either manually or using the command below):
   ```bash
   touch .env
   ```
2. Open the `.env` file and add the following lines:
   ```plaintext
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   SPOTIFY_REDIRECT_URI=http://localhost:4321
   ```
   Ensure that port `:4321` is available on your system.

3. Replace `your_client_id` and `your_client_secret` with the values you noted down in Step 1.

## Step 5: Run the Script

1. Run the script:

   - For Windows:
     ```powershell
     python main.py
     ```
   - For macOS/Linux:
     ```bash
     python3 main.py
     ```

2. You will be redirected to a Spotify authorization page. Click on **Agree** to authorize the app.
3. You will be redirected to a page that says "You can close this window now." Close the window.
4. A new file named `.cache` will appear in the project directory. This file contains your refresh token (and an access token with an expiration time).

Congratulations! You have successfully stored your Spotify refresh token using Spotipy. You can now use this token to access the Spotify API on behalf of the authenticated user.

**Important**: Keep your `.env` file containing your credentials and the `.cache` file secure and do not share them with others.

---

If you have any further questions, feel free to ask!

## Special Thanks

Special thanks to @vimfm for the original script.

# Happy Coding! 🚀