import streamlit as st
import google.generativeai as genai

# タイトル
st.set_page_config(page_title="投資AI ハレケ", page_icon="📈")
st.title("📈 投資AI ハレケ")

# --- 🔐 パスワード機能 ---
if "APP_PASSWORD" not in st.secrets:
    st.error("管理者に連絡してパスワードを設定してくれ！")
    st.stop()

password_input = st.text_input("🔑 パスワードを入力してね", type="password")

if password_input != st.secrets["APP_PASSWORD"]:
    if password_input:
        st.error("パスワードが違うぜ！")
    st.stop()

st.success("ログイン成功！ようこそハレケへ。")
# --- パスワード機能ここまで ---

# ★APIキー設定（現在無料で動く最新版 gemini-2.5-flash に変更！）
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-2.5-flash')
else:
    st.error("APIキーが設定されてないぜ！")
    st.stop()

# 入力欄
news_text = st.text_area("📰 ニュース本文を貼り付けてね", height=250)

if st.button("ハレケで分析する"):
    if news_text:
        with st.spinner("ハレケAIが市場を分析中..."):
            prompt = f"以下のニュースを投資家目線でポジ・ネガ判定し、3つの要点で簡潔にまとめて：\n\n{news_text}"
            try:
                response = model.generate_content(prompt)
                st.success("分析完了だぜ！")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"エラーだぜ: {e}")
    else:
        st.warning("ニュースをコピペしてくれ！")
