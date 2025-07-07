import os
from supabase import create_client

SUPABASE_URL = ""
SUPABASE_KEY = ""

# NOMBRE DEL BLOQUE PARA TU STORAGE
BUCKET_HONGO = ""
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)