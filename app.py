import streamlit as st
import google.generativeai as genai

# タイトル
st.set_page_config(page_title="ハレケラボ AIアナリスト", page_icon="📈")
st.title("📈 投資ニュース一発判定")

# --- 🔐 ここからパスワード機能 ---
if "APP_PASSWORD" not in st.secrets:
    st.error("管理者に連絡してパスワードを設定してくれ！")
    st.stop()

# パスワード入力欄
password_input = st.text_input("🔑 パスワードを入力してね", type="password")

if password_input != st.secrets["APP_PASSWORD"]:
    if password_input: # 入力されたけど間違っている場合
        st.error("パスワードが違うぜ！")
    st.stop() # 正解するまで下には進ませない

st.success("ログイン成功！さあ、分析を始めよう。")
# --- パスワード機能ここまで ---

# ★隠し場所（Secrets）からAPIキーを読み込む
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-2.5-flash')
else:
    st.error("APIキーが設定されてないぜ！")
    st.stop()

# 入力欄
news_text = st.text_area("📰 ニュース本文を貼り付けてね", height=250)

if st.button("AIで判定する"):
    if news_text:
        with st.spinner("プロのアナリストが分析中..."):
            prompt = f"以下のニュースを投資家目線でポジ・ネガ判定し、3つの要点でまとめて：\n\n{news_text}"
            try:
                response = model.generate_content(prompt)
                st.success("分析完了！")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"エラーだぜ: {e}")
    else:
        st.warning("ニュースをコピペしてくれ！")
