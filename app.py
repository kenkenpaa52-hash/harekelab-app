import streamlit as st
import google.generativeai as genai

# タイトル
st.set_page_config(page_title="ハレケラボ AIアナリスト", page_icon="📈")
st.title("📈 投資ニュース一発判定")

# 剣悟の鍵をセット
genai.configure(api_key="AIzaSyBt6fPQE0GvjmC9TIvwn-KxzeRcr9cacDI")
model = genai.GenerativeModel('gemini-2.5-flash')

# 入力欄
news_text = st.text_area("📰 ニュース本文を貼り付けてね", height=250)

if st.button("AIで判定する"):
    if news_text:
        with st.spinner("プロのアナリストが分析中..."):
            prompt = f"""
            あなたはプロの投資家です。以下のニュースを分析してください。
            1. 相場への影響（ポジティブ/ネガティブ/ニュートラル）
            2. その理由
            3. 投資家が注目すべきポイント3点
            
            【ニュース】
            {news_text}
            """
            try:
                response = model.generate_content(prompt)
                st.success("分析完了！")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"エラーだぜ: {e}")
    else:
        st.warning("ニュースをコピペしてくれ！")
