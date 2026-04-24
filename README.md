# My Userbot 🤖

Simple Pyrogram userbot — Termux pe chalao, apne account se kaam karo.

---

## ⚙️ Setup

### Step 1 — API credentials lo
1. https://my.telegram.org pe jao
2. **API development tools** → App create karo
3. `API_ID` aur `API_HASH` copy karo

### Step 2 — `userbot.py` mein bharo
```python
API_ID   = 12345678
API_HASH = "abcdef1234567890abcdef1234567890"
```

### Step 3 — Termux mein install karo
```bash
pkg update && pkg upgrade
pkg install python git
pip install -r requirements.txt
```

### Step 4 — Pehli baar login
```bash
python userbot.py
```
Phone number + OTP maangega → login ho jaoge → `my_userbot.session` file ban jaayegi

---

## ▶️ Chalao

```bash
python userbot.py
```

Background mein chalana ho toh:
```bash
nohup python userbot.py &
```

---

## 🗂️ Commands (prefix: `.`)

| Command | Kaam |
|---------|------|
| `.ping` | Bot alive check |
| `.id` | Chat/User ID dekho |
| `.info` | User ki info |
| `.del` | Replied message delete |
| `.purge <n>` | Last N apne messages delete |
| `.save` | Saved Messages mein save karo |
| `.tr <text>` | English mein translate |
| `.help` | Commands list |

---

## 📁 Structure

```
another/
├── userbot.py          ← Main file — yahi chalao
├── utils/
│   └── gen_session.py  ← Session string generate karne ke liye (optional)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚠️ Note
- `my_userbot.session` file secret rakho — GitHub pe push mat karna (.gitignore mein hai)
- Ye **userbot** hai — apne personal Telegram account se chalega
