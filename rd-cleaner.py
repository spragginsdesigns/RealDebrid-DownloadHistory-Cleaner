import aiohttp
import asyncio

# Replace 'YOUR_API_TOKEN' with your Real-Debrid API token
API_TOKEN = 'YOUR_API_TOKEN'
BASE_URL = 'https://api.real-debrid.com/rest/1.0/downloads'


async def fetch_downloads(session, page=1):
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
    downloads = []
    while True:
        async with session.get(f"{BASE_URL}?page={page}", headers=headers) as response:
            if response.status == 200:
                page_downloads = await response.json()
                if not page_downloads:
                    break
                downloads.extend(page_downloads)
                page += 1
            else:
                print(f"Failed to fetch downloads. Status Code: {response.status}")
                break
    return downloads


async def delete_download(session, download_id, filename):
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
    async with session.delete(f"{BASE_URL}/delete/{download_id}", headers=headers) as response:
        if response.status == 204:
            print(f"Successfully deleted: {filename}")
        else:
            print(f"Failed to delete: {filename} - Status Code: {response.status}")


async def clear_download_history():
    async with aiohttp.ClientSession() as session:
        print("Fetching the list of downloads...")
        downloads = await fetch_downloads(session)

        if not downloads:
            print("Your download history is already empty.")
            return

        print(f"Found {len(downloads)} downloads in your history.")
        for download in downloads:
            print(f"Filename: {download['filename']}")

        confirm_clear = input("Do you want to delete all these downloads from your history? (yes/no): ").strip().lower()
        if confirm_clear == 'yes':
            tasks = []
            for download in downloads:
                print(f"Deleting download: {download['filename']}")
                tasks.append(delete_download(session, download['id'], download['filename']))
            await asyncio.gather(*tasks)

            # Verify that the download history is now empty
            print("Verifying that the download history is empty...")
            updated_downloads = await fetch_downloads(session)
            if not updated_downloads:
                print("All downloads have been deleted from your history.")
            else:
                print("Some downloads are still present in the history:")
                for download in updated_downloads:
                    print(f"Filename: {download['filename']}")
        else:
            print("No downloads were deleted.")


def main():
    print("Welcome to Real-Debrid Download History Cleaner")
    start_clear = input(
        "Do you want to start the process of clearing your download history? (yes/no): ").strip().lower()
    if start_clear == 'yes':
        asyncio.run(clear_download_history())
    else:
        print("Process aborted. No changes were made.")


if __name__ == "__main__":
    main()
