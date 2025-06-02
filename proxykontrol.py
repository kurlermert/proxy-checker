import asyncio
import aiohttp
import time
import tkinter as tk
from tkinter import ttk, scrolledtext


TEST_URL = "https://www.knightonline.world"

class ProxyCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Proxy Checker")
        self.root.geometry("600x500")
        self.root.configure(bg="#1e1e1e")
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", background="#007acc", foreground="white", font=("Segoe UI", 10, "bold"))
        style.map("TButton", background=[("active", "#005f99")])

        title_label = tk.Label(self.root, text="Proxy Checker", bg="#1e1e1e", fg="white", font=("Segoe UI", 14, "bold"))
        title_label.pack(pady=10)

        self.entry = scrolledtext.ScrolledText(self.root, width=70, height=10, bg="#2d2d2d", fg="white", insertbackground="white", font=("Consolas", 10))
        self.entry.pack(pady=10)

        check_button = ttk.Button(self.root, text="Check Proxies", command=self.start_check)
        check_button.pack(pady=5)

        self.output = scrolledtext.ScrolledText(self.root, width=70, height=15, bg="#2d2d2d", fg="white", state="disabled", font=("Consolas", 10))
        self.output.pack(pady=10)

    def log(self, message, color="white"):
        self.output.configure(state="normal")
        self.output.insert(tk.END, message + "\n")
        self.output.tag_add(color, "end-2l", "end-1l")
        self.output.tag_config("green", foreground="lightgreen")
        self.output.tag_config("red", foreground="red")
        self.output.see(tk.END)
        self.output.configure(state="disabled")

    def start_check(self):
        proxies = self.entry.get("1.0", tk.END).strip().splitlines()
        self.output.configure(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.configure(state="disabled")
        asyncio.run(self.check_proxies(proxies))

    async def check_single_proxy(self, session, proxy, auth):
        start = time.perf_counter()
        try:
            async with session.get(TEST_URL, proxy=proxy, proxy_auth=auth, timeout=10) as response:
                elapsed = int((time.perf_counter() - start) * 1000)
                if response.status == 200:
                    self.log(f"{proxy} - ✓  - {elapsed}ms  - OK", "green")
                else:
                    self.log(f"{proxy} - ✗  - {elapsed}ms  - HATALI CEVAP", "red")
        except aiohttp.ClientHttpProxyError:
            self.log(f"{proxy} - ✗  - Proxy kimlik doğrulama hatası", "red")
        except asyncio.TimeoutError:
            self.log(f"{proxy} - ✗  - ZAMAN AŞIMI", "red")
        except Exception as e:
            self.log(f"{proxy} - ✗  - {str(e)}", "red")

    async def check_proxies(self, proxy_list):
        connector = aiohttp.TCPConnector(ssl=False)
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = []
            for line in proxy_list:
                try:
                    ip_port, user_pass = line.strip().split()
                    user, passwd = user_pass.split(":")
                    proxy_url = f"http://{user}:{passwd}@{ip_port}"
                    auth = aiohttp.BasicAuth(user, passwd)
                    tasks.append(self.check_single_proxy(session, proxy_url, auth))
                except ValueError:
                    self.log(f"Format Hatalı: {line}", "red")
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProxyCheckerApp(root)
    root.mainloop()
