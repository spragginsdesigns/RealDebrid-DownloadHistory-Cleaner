# RealDebrid-DownloadHistory-Cleaner

This Python script helps you efficiently clear your Real-Debrid download history using the Real-Debrid API. It leverages `asyncio` and `aiohttp` for concurrent requests, making the deletion process faster.

## Features

- Fetches all downloads from your Real-Debrid account, handling pagination to ensure all downloads are retrieved.
- Displays a list of downloads and asks for user confirmation before deletion.
- Deletes all confirmed downloads concurrently.
- Verifies the deletion by re-fetching the download history.

## Requirements

- Python 3.7+
- `aiohttp` library

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/spragginsdesigns/RealDebrid-DownloadHistory-Cleaner.git
   cd RealDebrid-DownloadHistory-Cleaner
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```sh
   pip install aiohttp
   ```

## Configuration

Replace `'YOUR_API_TOKEN'` with your actual Real-Debrid API token in the script. You can obtain your API token from [Real-Debrid API Token](https://real-debrid.com/apitoken).

```python
API_TOKEN = 'YOUR_API_TOKEN'
```

## Usage

Run the script using Python:

```sh
python rd-cleaner.py
```

Follow the prompts:

- The script will ask if you want to start the process of clearing your download history.
- If you choose 'yes', it will fetch and display all downloads in your history.
- It will then ask for confirmation before deleting all the entries concurrently.
- After attempting to delete the downloads, it will fetch the download history again to verify that it is empty and display the result.

## Example

```sh
Welcome to Real-Debrid Download History Cleaner
Do you want to start the process of clearing your download history? (yes/no): yes
Fetching the list of downloads...
Found 150 downloads in your history.
Filename: ExampleFile1.mkv
Filename: ExampleFile2.mkv
...
Do you want to delete all these downloads from your history? (yes/no): yes
Deleting download: ExampleFile1.mkv
Deleting download: ExampleFile2.mkv
...
Verifying that the download history is empty...
All downloads have been deleted from your history.
```

## Real-Debrid API Documentation

This script uses the Real-Debrid API to manage your download history. For more detailed information about the API, refer to the [Real-Debrid API Documentation](https://api.real-debrid.com/).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact `austin@spragginsdesigns.xyz`.

---

### Notes

- Ensure you have a valid Real-Debrid API token.
- The script handles pagination to ensure all downloads are fetched and deleted.
- The script uses asynchronous operations for faster execution.
