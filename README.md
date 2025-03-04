# Flask_web
เว็บไซต์แบรนด์รถยนต์
นี่คือเว็บแอปพลิเคชันที่พัฒนาด้วย Flask สำหรับแสดงข้อมูลเกี่ยวกับแบรนด์รถยนต์ต่างๆ ผู้ใช้สามารถเรียกดูรุ่นรถที่หลากหลาย ดูข้อมูลรายละเอียด และเพิ่มรถที่ชื่นชอบไปยังรายการโปรดของตนเองได้ แอปพลิเคชันนี้ยังมีระบบล็อกอิน/สมัครสมาชิก และหน้าโปรไฟล์สำหรับจัดการรถที่ชื่นชอบของผู้ใช้

คุณสมบัติ
ระบบผู้ใช้: สามารถสมัครสมาชิก, เข้าสู่ระบบ และออกจากระบบได้
หน้าข้อมูลแบรนด์รถยนต์: มีหน้าแสดงแบรนด์รถยนต์ (Ferrari, Lamborghini, Porsche) พร้อมรายละเอียดของแต่ละรุ่น
รายการรถที่ชื่นชอบ: ผู้ใช้สามารถเพิ่มหรือลบรถจากรายการโปรดของตนเองได้
หน้าโปรไฟล์: ผู้ใช้สามารถดูและจัดการรถที่ชื่นชอบได้จากหน้าโปรไฟล์
รองรับทุกอุปกรณ์: เว็บไซต์ถูกออกแบบให้รองรับทั้งเดสก์ท็อปและมือถือ
เทคโนโลยีที่ใช้
Flask: เว็บเฟรมเวิร์กสำหรับ Python
SQLAlchemy: ไลบรารี ORM สำหรับจัดการฐานข้อมูล
Flask-Login: ระบบจัดการการรับรองตัวตนและเซสชันของผู้ใช้
Bootstrap: เฟรมเวิร์กสำหรับออกแบบเว็บที่ตอบสนองทุกอุปกรณ์
WTForms: ไลบรารีสำหรับจัดการฟอร์มในเว็บแอปพลิเคชัน

โครงสร้างโปรเจ็กต์
csharp
คัดลอก
แก้ไข
car-brand-website/
│
├── acl.py                # จัดการสิทธิ์การเข้าถึง
├── forms.py              # ฟอร์มที่ใช้ WTForms
├── models.py             # โมเดลฐานข้อมูล (SQLAlchemy)
├── main.py               # ไฟล์หลักของแอปพลิเคชัน
├── README.md             # ไฟล์รายละเอียดโปรเจ็กต์
├── requirements.txt      # รายการไลบรารีที่ต้องติดตั้ง
├── static/               # ไฟล์สื่อ เช่น CSS, JavaScript, รูปภาพ
│   ├── css/
│   ├── images/
│   └── js/
└── templates/            # ไฟล์ HTML สำหรับแสดงผล
    ├── base.html         # เทมเพลตรูปแบบหลัก
    ├── brand.html        # หน้าแบรนด์รถยนต์
    ├── Carrera_GT.html   # หน้ารถ Porsche Carrera GT
    ├── ferrari.html      # หน้ารถ Ferrari
    ├── ferrari_j50.html  # หน้ารถ Ferrari J50
    ├── Ferrari_LaFerrari_Aperta_2016.html  # หน้ารถ Ferrari LaFerrari Aperta 2016
    ├── Ferrari_LaFerrari_Coupe_2013.html   # หน้ารถ Ferrari LaFerrari Coupe 2013
    ├── index.html        # หน้าแรก
    ├── Lamborghini.html  # หน้ารถ Lamborghini
    ├── Lamborghini_Huracán.html  # หน้ารถ Lamborghini Huracán
    ├── Lamborghini_Reventón.html # หน้ารถ Lamborghini Reventón
    ├── Lamborghini_Veneno.html   # หน้ารถ Lamborghini Veneno
    ├── login.html        # หน้าเข้าสู่ระบบ
    ├── navbar.html       # เมนูนำทาง
    ├── porsche.html      # หน้ารถ Porsche
    ├── porsche_911_GT3_RS.html  # หน้ารถ Porsche 911 GT3 RS
    ├── Porsche_918_Spyder.html  # หน้ารถ Porsche 918 Spyder
    ├── profile.html      # หน้าโปรไฟล์ผู้ใช้
    └── register.html     # หน้าสมัครสมาชิก
วิธีใช้งาน
หน้าแรก: แสดงภาพสไลด์และลิงก์ไปยังแบรนด์รถยนต์ต่างๆ
หน้าข้อมูลแบรนด์: แต่ละแบรนด์ (Ferrari, Lamborghini, Porsche) มีรายชื่อรุ่นรถพร้อมรายละเอียด
หน้ารายละเอียดรถ: แสดงข้อมูลเชิงลึกเกี่ยวกับรถแต่ละรุ่น รวมถึงเครื่องยนต์, แรงม้า และแรงบิด ผู้ใช้สามารถเพิ่มรถลงในรายการโปรดได้
หน้าโปรไฟล์: ผู้ใช้สามารถดูและจัดการรถที่ชื่นชอบได้
การมีส่วนร่วม (Contributing)
ยินดีต้อนรับทุกการมีส่วนร่วม! สามารถ fork โปรเจ็กต์ และสร้าง pull request พร้อมกับการเปลี่ยนแปลงของคุณได้

ใบอนุญาต
โปรเจ็กต์นี้ได้รับอนุญาตภายใต้ MIT License

ขอบคุณแหล่งข้อมูล
Flask Documentation
Bootstrap Documentation
SQLAlchemy Documentation