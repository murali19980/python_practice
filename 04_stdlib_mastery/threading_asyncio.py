"""
Practice: Concurrency (Threading & Asyncio)
"""
import threading
import asyncio
import time

# Threading version
def download_site_thread(url):
    print(f"[Thread] Starting download of {url}")
    time.sleep(1)
    print(f"[Thread] Finished download of {url}")

# Asyncio version
async def download_site_async(url):
    print(f"[Async] Starting download of {url}")
    await asyncio.sleep(1)
    print(f"[Async] Finished download of {url}")

async def run_async_downloads(urls):
    tasks = [download_site_async(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = ["site1.com", "site2.com", "site3.com"]
    
    print("--- Threading Demo ---")
    threads = []
    for url in urls:
        t = threading.Thread(target=download_site_thread, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("All threaded downloads complete.\n")

    print("--- Asyncio Demo ---")
    asyncio.run(run_async_downloads(urls))
    print("All async downloads complete.")
