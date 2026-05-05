"""
Script seed data TPS statis ke database.
Jalankan: python scripts/seed_locations.py

Tambah data TPS real dari kotamu di list LOCATIONS_DATA.
"""

import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sortify.settings")
django.setup()

from apps.locations.models import Location

LOCATIONS_DATA = [
    {
        "name": "Bank Sampah Induk Jakarta Pusat",
        "facility_type": "BANK_SAMPAH",
        "city": "Jakarta Pusat",
        "province": "DKI Jakarta",
        "address": "Jl. Rawasari Sel. No.35, RT.16/RW.2, Cemp. Putih Tim., Kec. Cemp. Putih, Kota Jakarta Pusat, Daerah Khusus Ibukota Jakarta 10510",
        "phone": "+62 878-1111-1111",
        "maps_url": "https://maps.google.com/?cid=2748793522150338415",
    },
    {
        "name": "Bank Sampah Hijau Selaras Mandiri",
        "facility_type": "BANK_SAMPAH",
        "city": "Jakarta Pusat",
        "province": "DKI Jakarta",
        "address": "Kompleks Angkasa Pura Blok PQRS RT:14 RW:06 Kelurahan, RT.14/RW.11, Kebon Kosong, Kemayoran, Central Jakarta City, Jakarta 10630",
        "phone": "+62 813-1874-7789",
        "maps_url": "https://maps.google.com/?cid=16566894765364376484",
    },
    {
        "name": "Bank Sampah H.Mo'ong Dalam",
        "facility_type": "BANK_SAMPAH",
        "city": "Jakarta Timur",
        "province": "DKI Jakarta",
        "address": "Jl. Kobangdiklat I No.47, RT.3/RW.7, Baru, Kec. Ps. Rebo, Kota Jakarta Timur, Daerah Khusus Ibukota Jakarta 13780",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=1358165073577980213",
    },
    {
        "name": "Bank sampah JATISEBELAS",
        "facility_type": "BANK_SAMPAH",
        "city": "Jakarta Timur",
        "province": "DKI Jakarta",
        "address": "Jl. Dato Tonggara IV Gg. Alam Indah I No.76, RT.4/RW.11, Kramat Jati, Kec. Kramat jati, Kota Jakarta Timur, Daerah Khusus Ibukota Jakarta 13510",
        "phone": "+62 821-1028-6669",
        "maps_url": "https://maps.google.com/?cid=14815080613140044456",
    },
    {
        "name": "Bank Sampah Anggrek Ciliwung",
        "facility_type": "BANK_SAMPAH",
        "city": "Jakarta Selatan",
        "province": "DKI Jakarta",
        "address": "Jakarta Selatan, RT.7/RW.1, Srengseng Sawah, Kec. Jagakarsa, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12645",
        "phone": "+62 21 72737550",
        "maps_url": "https://maps.google.com/?cid=2159577683271769848",
    },
    {
        "name": "Bank Sampah Jambu Muda",
        "facility_type": "BANK_SAMPAH",
        "city": "Jakarta Selatan",
        "province": "DKI Jakarta",
        "address": "Jl. Jambu II No.50, RT.3/RW.2, Cipedak, Kec. Jagakarsa, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12630",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=570483345782518177",
    },
    {
        "name": "Bank Sampah Induk Satu Hati Jakarta Barat",
        "facility_type": "BANK_SAMPAH",
        "city": "Jakarta Barat",
        "province": "DKI Jakarta",
        "address": "Blk. B, RT.5/RW.5, Cengkareng Bar., Kecamatan Cengkareng, Kota Jakarta Barat, Daerah Khusus Ibukota Jakarta 11830",
        "phone": "+62 21 56972948",
        "maps_url": "https://maps.google.com/?cid=13349872772297961863",
    },
    {
        "name": "BANK SAMPAH 2890",
        "facility_type": "BANK_SAMPAH",
        "city": "Jakarta Barat",
        "province": "DKI Jakarta",
        "address": "RQQH+46M, Jl. Sosial, RT.8/RW.2, Wijaya Kusuma, Kec. Grogol petamburan, Kota Jakarta Barat, Daerah Khusus Ibukota Jakarta 11460",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=8301564024079062764",
    },
    {
        "name": "Bank Sampah Induk Kumala",
        "facility_type": "BANK_SAMPAH",
        "city": "Jakarta Utara",
        "province": "DKI Jakarta",
        "address": "Jl. Budi Jaya No.44, RT.1/RW.8, Sungai Bambu, Kec. Tj. Priok, Jkt Utara, Daerah Khusus Ibukota Jakarta 14330",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=9590533386116566829",
    },
    {
        "name": "Bank Sampah PCK Proklim Sunter Jaya",
        "facility_type": "BANK_SAMPAH",
        "city": "Jakarta Utara",
        "province": "DKI Jakarta",
        "address": "Komplek ruko, Jl. Sunter Jaya I blok c 88, RT.21/RW.1, Sunter Jaya, Kec. Tj. Priok, Jkt Utara, Daerah Khusus Ibukota Jakarta 14360",
        "phone": "+62 818-0825-3935",
        "maps_url": "https://maps.google.com/?cid=15147870724557281714",
    },
    {
        "name": "TPA Cipayung",
        "facility_type": "TPA",
        "city": "Depok",
        "province": "Jawa Barat",
        "address": "Jl. Pertanian Cipayungjaya No.50, Cipayung, Kec. Cipayung, Kota Depok, Jawa Barat 16437",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=682376698730634872",
    },
    {
        "name": "Bank Sampah Induk Rumah Harum Depok",
        "facility_type": "BANK_SAMPAH",
        "city": "Depok",
        "province": "Jawa Barat",
        "address": "Jl. Merdeka No.1, RT.05/RW.01, Abadijaya, Kec. Sukmajaya, Kota Depok, Jawa Barat 16411",
        "phone": "+62 853-1196-5509",
        "maps_url": "https://maps.google.com/?cid=6463051922727086419",
    },
    {
        "name": "Tempat Pembuangan Sampah (TPS) Pasar Kemiri",
        "facility_type": "TPS",
        "city": "Depok",
        "province": "Jawa Barat",
        "address": "JR7F+MQQ, Kemiri Muka, Kecamatan Beji, Kota Depok, Jawa Barat 16423",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=11673078335715611908",
    },
    {
        "name": "TPS Taman Puspa",
        "facility_type": "TPS",
        "city": "Depok",
        "province": "Jawa Barat",
        "address": "Jl. Kamboja No.15, Tugu, Kec. Cimanggis, Kota Depok, Jawa Barat 16451",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=13722552094167677889",
    },
    {
        "name": "Gunung Sampah (Mekarsari)",
        "facility_type": "TPS",
        "city": "Depok",
        "province": "Jawa Barat",
        "address": "JVQ6+WVJ, Mekarsari, Kec. Cimanggis, Kota Depok, Jawa Barat 16452",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=17246305223873956410",
    },
    {
        "name": "Kompos",
        "facility_type": "PENGOLAHAN_SAMPAH",
        "city": "Depok",
        "province": "Jawa Barat",
        "address": "HRW5+CHM, Pancoran Mas, Kec. Pancoran Mas, Kota Depok, Jawa Barat 16436",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=6519181864742946305",
    },
    {
        "name": "TPA GALUGA",
        "facility_type": "TPA",
        "city": "Bogor",
        "province": "Jawa Barat",
        "address": "CJMV+M79, Galuga, Kec. Cibungbulang, Kabupaten Bogor, Jawa Barat 16630",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=1825847103238040009",
    },
    {
        "name": "TPST Mutiara Bogor Raya",
        "facility_type": "TPS",
        "city": "Bogor",
        "province": "Jawa Barat",
        "address": "9RFM+V33, RT.04/RW.16, Katulampa, Kec. Bogor Tim., Kota Bogor, Jawa Barat 16144",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=14340871457461324422",
    },
    {
        "name": "TPS 3R Kelurahan Mulyaharja, Kota Bogor",
        "facility_type": "TPS",
        "city": "Bogor",
        "province": "Jawa Barat",
        "address": "Blok, Jl. Kabayan 1 Gg. Anggrek No.57, RT.05/RW.03, Mulyaharja, Bogor Selatan, Bogor City, West Java 16135",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=11999750795331953351",
    },
    {
        "name": "TPS 3R KSM Kencana Permai",
        "facility_type": "TPS",
        "city": "Bogor",
        "province": "Jawa Barat",
        "address": "Jl. Perumahan Bumi Kencana Permai, RT.04/RW.10, Tanah Sareal, Kota Bogor, Jawa Barat 16167",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=6635340327138097567",
    },
    {
        "name": "Bank Sampah Pusat Kabupaten Bogor",
        "facility_type": "BANK_SAMPAH",
        "city": "Bogor",
        "province": "Jawa Barat",
        "address": "Jl. TPA Pd. Rajeg, Pd. Rajeg, Kec. Cibinong, Kabupaten Bogor, Jawa Barat 16413",
        "phone": "+62 812-8108-0237",
        "maps_url": "https://maps.google.com/?cid=7812626705061197915",
    },
    {
        "name": "Bank Sampah Barokah Bogor",
        "facility_type": "BANK_SAMPAH",
        "city": "Bogor",
        "province": "Jawa Barat",
        "address": "CRM3+5XQ, RT.02, Jl. Dadali Lb., RT.02 RW05/RW.05, Kedungbadak, Tanah Sareal, Kota Bogor, Jawa Barat 16161",
        "phone": "+62 888-2999-111",
        "maps_url": "https://maps.google.com/?cid=835786961838801993",
    },
    {
        "name": "Bank Sampah Kenanga Kota Bogor",
        "facility_type": "BANK_SAMPAH",
        "city": "Bogor",
        "province": "Jawa Barat",
        "address": "CR44+436, Jl. Bogor, RT.01/RW.01, Babakan, Kecamatan Bogor Tengah, Kota Bogor, Jawa Barat 16128",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=2473688539302011057",
    },
    {
        "name": "Bank Sampah VIDA Bekasi",
        "facility_type": "BANK_SAMPAH",
        "city": "Bekasi",
        "province": "Jawa Barat",
        "address": "Jl. Taman Apel Hijau I No.69, RT.002/RW.001, Padurenan, Kec. Mustika Jaya, Kota Bks, Jawa Barat 16340",
        "phone": "+62 813-1723-6600",
        "maps_url": "https://maps.google.com/?cid=17992236951997688028",
    },
    {
        "name": "TPST Bantar Gebang",
        "facility_type": "TPST",
        "city": "Bekasi",
        "province": "Jawa Barat",
        "address": "RT.002/RW.005, Ciketing Udik, Kec. Bantar Gebang, Kota Bks, Jawa Barat 17153",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=9646851261211929389",
    },
    {
        "name": "TPS3R KPP BINA LINDUNG",
        "facility_type": "TPS",
        "city": "Bekasi",
        "province": "Jawa Barat",
        "address": "Komplek Bina Lindung, Jl. Binasiswa l, RT.005/RW.011, Jaticempaka, Kec. Jaticempaka, Kota Bks, Jawa Barat 17411",
        "phone": "+62 813-1109-9171",
        "maps_url": "https://maps.google.com/?cid=6140267540123044598",
    },
    {
        "name": "Bank Sampah Sumber Mutiara Tangerang",
        "facility_type": "BANK_SAMPAH",
        "city": "Tangerang",
        "province": "Banten",
        "address": "Jl. Lembang II Lama Jl. Onar, RT.04/RW.008, Sudimara Bar., Kec. Ciledug, Kota Tangerang, Banten 15151",
        "phone": "+62 877-7721-6986",
        "maps_url": "https://maps.google.com/?cid=5543650924298637148",
    },
    {
        "name": "Bank Sampah 102",
        "facility_type": "BANK_SAMPAH",
        "city": "Tangerang",
        "province": "Banten",
        "address": "Jamblang II No.102, RT.004/RW.015, Cibodasari, Kec. Cibodas, Kota Tangerang, Banten 15138",
        "phone": "+62 812-1000-679",
        "maps_url": "https://maps.google.com/?cid=10502356051339808103",
    },
    {
        "name": "Bank Sampah Induk Kabupaten Tangerang",
        "facility_type": "BANK_SAMPAH",
        "city": "Tangerang",
        "province": "Banten",
        "address": "MHV9+P8H, RT.01/RW.02, Palasari, Kec. Legok, Kabupaten Tangerang, Banten 15820",
        "phone": "+62 819-0816-4858",
        "maps_url": "https://maps.google.com/?cid=3807660537416785220",
    },
    {
        "name": "Bank Sampah Induk Cabang Sadang Serang",
        "facility_type": "BANK_SAMPAH",
        "city": "Bandung",
        "province": "Jawa Barat",
        "address": "Jl. Sadang Tengah No.6, Sekeloa, Kecamatan Coblong, Kota Bandung, Jawa Barat 40133",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=1813048655413301612",
    },
    {
        "name": "bank sampah resik babakan sari",
        "facility_type": "BANK_SAMPAH",
        "city": "Bandung",
        "province": "Jawa Barat",
        "address": "Jl. Babakan Sari No.64, Babakan Sari, Kec. Kiaracondong, Kota Bandung, Jawa Barat 40272",
        "phone": "+62 812-1063-5356",
        "maps_url": "https://maps.google.com/?cid=9661260223273663425",
    },
    {
        "name": "Bank sampah induk kota bandung",
        "facility_type": "BANK_SAMPAH",
        "city": "Bandung",
        "province": "Jawa Barat",
        "address": "Blk. B-C No.c27, Jatihandap, Kec. Mandalajati, Kota Bandung, Jawa Barat 40195",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=9917828905752978606",
    },
    {
        "name": "Bank Sampah Bumi Inpirasi",
        "facility_type": "BANK_SAMPAH",
        "city": "Bandung",
        "province": "Jawa Barat",
        "address": "Jl. Cisitu Indah VI No.188, Dago, Kecamatan Coblong, Kota Bandung, Jawa Barat 40135",
        "phone": "+62 22 2504040",
        "maps_url": "https://maps.google.com/?cid=1944480724481369332",
    },
    {
        "name": "TPS Terpadu Babakan Sari",
        "facility_type": "TPS",
        "city": "Bandung",
        "province": "Jawa Barat",
        "address": "Jl. Babakan Sari No.64, Babakan Sari, Kec. Kiaracondong, Kota Bandung, Jawa Barat 40272",
        "phone": "+62 823-1500-0080",
        "maps_url": "https://maps.google.com/?cid=14034901366931068647",
    },
    {
        "name": "Pengolahan Sampah (TPS Sauyunan Hegarmanah)",
        "facility_type": "TPS",
        "city": "Jatinangor",
        "province": "Jawa Barat",
        "address": "Jl. Raya Jatinangor No.230, Hegarmanah, Kec. Jatinangor, Kabupaten Sumedang, Jawa Barat 45363",
        "phone": "+62 853-2244-3332",
        "maps_url": "https://maps.google.com/?cid=7125540769998082359",
    },
    {
        "name": "TPS Cluster Alamanda",
        "facility_type": "TPS",
        "city": "Jatinangor",
        "province": "Jawa Barat",
        "address": "3Q2X+V99, Alamanda V, Cisempur, Kec. Jatinangor, Kabupaten Sumedang, Jawa Barat 45363",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=14606866469371080520",
    },
    {
        "name": "TPS 1 DESA CILELES",
        "facility_type": "TPS",
        "city": "Jatinangor",
        "province": "Jawa Barat",
        "address": "3QHH+7RX, Cileles, Kec. Jatinangor, Kabupaten Sumedang, Jawa Barat 45363",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=17618089299573449198",
    },
    {
        "name": "TPS3R Cileles Smart",
        "facility_type": "TPS",
        "city": "Jatinangor",
        "province": "Jawa Barat",
        "address": "3QPG+34X, Jl. Cilayung, Cileles, Kec. Jatinangor, Kabupaten Sumedang, Jawa Barat 45363",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=13863249724350565549",
    },
    {
        "name": "TPA Darusy Syahid",
        "facility_type": "TPA",
        "city": "Jatinangor",
        "province": "Jawa Barat",
        "address": "Jl. Cipacing Dusun Bojong euren tengah No.53, RT.01/RW.12, Cibeusi, Kec. Jatinangor, Kabupaten Sumedang, Jawa Barat 45363",
        "phone": "-",
        "maps_url": "https://maps.google.com/?cid=14639052112723125874",
    },
]


def seed():
    created = 0
    skipped = 0

    for data in LOCATIONS_DATA:
        obj, is_new = Location.objects.get_or_create(
            name=data["name"],
            city=data["city"],
            defaults=data,
        )
        if is_new:
            created += 1
            print(f"  Created: {obj.name} - {obj.city}")
        else:
            skipped += 1
            print(f"   Exists:  {obj.name} - {obj.city}")

    print(f"\nSelesai! {created} data baru, {skipped} sudah ada.")


if __name__ == "__main__":
    print("Seeding data lokasi TPS...\n")
    seed()