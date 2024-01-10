import streamlit as st
import pandas as pd
import streamlit.components.v1 as stc
import numpy as np

def supplement_kind(df,v_purpose):
    if '有酸素運動' in v_purpose:
        re_df = df[df['運動目的'].isin(['有酸素運動'])]
        re_df = df[df['運動目的'].str.contains('有酸素運動')]
        # result_df = video_df[video_df['title'].str.contains(name)]
    elif 'ストレッチ'in v_purpose:
        re_df = df[df['運動目的'].isin(['ストレッチ'])]
        re_df = df[df['運動目的'].str.contains('ストレッチ')]
    elif '無酸素運動'in v_purpose:
        re_df = df[df['運動目的'].isin(['無酸素運動'])]
        re_df = df[df['運動目的'].str.contains('無酸素運動')]
    elif 'バランス'in v_purpose:
        re_df = df[df['運動目的'].isin(['有酸素運動','ストレッチ','無酸素運動'])]
        re_df = df[df['運動目的'].str.contains('有酸素運動|ストレッチ|無酸素運動')]
    elif 'ストレッチ・有酸素運動'in v_purpose:
        re_df = df[df['運動目的'].isin(['有酸素運動'])]
        re_df = df[df['運動目的'].str.contains('有酸素運動')]
    elif '無酸素運動・有酸素運動'in v_purpose:
        re_df = df[df['運動目的'].isin(['有酸素運動','無酸素運動'])]
        re_df = df[df['運動目的'].str.contains(['有酸素運動|無酸素運動'])]

    return re_df.head(10)

def supplement_name(df,purpose):
    if '無酸素運動' in purpose:
        re_df = df[df['運動目的2'].str.contains('無酸素運動')]
    elif 'ストレッチ'in purpose:
        re_df = df[df['運動目的2'].str.contains('ストレッチ')]
    elif '有酸素運動'in purpose:
        re_df = df[df['運動目的2'].str.contains('有酸素運動')]
    elif 'バランス'in purpose:
        re_df = df[df['運動目的2'].str.contains('バランス')]
    elif 'ストレッチ・有酸素運動'in purpose:
        re_df = df[df['運動目的2'].str.contains('ストレッチ・有酸素運動')]
    elif '無酸素運動・有酸素運動'in purpose:
        re_df = df[df['運動目的2'].str.contains('無酸素運動・有酸素運動')]

    return re_df.head(5)

def supplement_enter(s_df,s_select):
    normal_df = s_df[(s_df['商品名'] == s_select)]
    purpose = normal_df['運動目的2'].values[0]
    return purpose
def split_10(df):
    
    # Pandas DataFrameを行方向に10行毎に分割する
    df_list = []
    split_num = 10
    while True:
    # 分割数までの行数を抽出する
        df_buf = df[:split_num]
        
        # データフレームをリストへ格納
        df_list.append(df_buf)
        
        # 分割数以降の行数をdf2へ格納する
        df = df[split_num:]
        
        # もし、データフレームが空の場合、ループを抜ける
        if df.empty:
            break

    return df_list

def split_5(df):
    
    # Pandas DataFrameを行方向に10行毎に分割する
    df_list = []
    split_num = 5
    while True:
    # 分割数までの行数を抽出する
        df_buf = df[:split_num]
        
        # データフレームをリストへ格納
        df_list.append(df_buf)
        
        # 分割数以降の行数をdf2へ格納する
        df = df[split_num:]
        
        # もし、データフレームが空の場合、ループを抜ける
        if df.empty:
            break

    return df_list

def search(df):
    for i in range(len(df)):
    # タイトル
        st.markdown(f"### {df['title'].values[i]}")
        id = df["videoId"].values[i]
        stc.html(f"""
            <iframe width="315" height="315" src="https://www.youtube.com/embed/{id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            """,height = 350)
        st.divider()

def supple_recommend(s_df,v_select,v_select2):
    supplement_df = supplement_kind(s_df,v_select)
    m_list = supplement_df['商品名'].unique().tolist()
    st.markdown("")
    st.markdown(f" ### {v_select2}におすすめのサプリはこちらです")
    num=10
    lcol=[]
    col= st.columns(num)
    for a in range(len(m_list)):
        with col[a]:
            st.caption(m_list[a])
            st.image(f"image/{m_list[a]}/{m_list[a]}_1.png")
            st.link_button("詳細",f"https://www.diet-cafe.jp/search_result.html?cx=partner-pub-6658419875952282%3A2007643100&q={m_list[a]}")

def supple_only_recommend(s_select):
    st.image(f"image/{s_select}/{s_select}_1.png")
    st.markdown(f"{s_select}")
    st.link_button("詳細",f"https://www.diet-cafe.jp/search_result.html?cx=partner-pub-6658419875952282%3A2007643100&q={s_select}")

def search_name(v_df,s_df):
    for i in range(len(v_df)):
    # タイトル
        st.markdown(f"### {v_df['title'].values[i]}")
        id = v_df["videoId"].values[i]
        stc.html(f"""
            <iframe width="315" height="315" src="https://www.youtube.com/embed/{id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            """,height = 350)
        supplement_df = supplement_name(s_df,v_df["運動目的"].values[i])
        m_list = supplement_df['商品名'].unique().tolist()
        num=5
        col_1= st.columns(num)
        for a in range(len(m_list)):
            with col_1[a]:
                st.caption(m_list[a])
                st.image(f"image/{m_list[a]}/{m_list[a]}_1.png", use_column_width=True)
                st.link_button("詳細",f"https://www.diet-cafe.jp/search_result.html?cx=partner-pub-6658419875952282%3A2007643100&q={m_list[a]}")
        st.divider()

def supple_search(df):
    for i in range(len(df)):
    # タイトル
        st.markdown(f"### {df['title'].values[i]}")
        id = df["videoId"].values[i]
        stc.html(f"""
            <iframe width="315" height="315" src="https://www.youtube.com/embed/{id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            """,height = 350)
        st.divider()    

def video_search_key(df,key):
    # '視聴回数','高評価数','コメント数'
    if key == '視聴回数':
        df = df.sort_values('viewCount', ascending=False)
    elif key == '高評価数':
        df = df.sort_values('likeCount', ascending=False)
    else:
        df = df.sort_values('commentCount', ascending=False)
    
    return df

def nutrients_supple_serch(n_select,s_df,n_df):
    try:
        df = n_df[(n_df['栄養素'] == n_select)]
        nutrients_name = df['栄養素'].values[0]
        nutrients_manual = df['説明文'].values[0]
        st.markdown(f"#### {nutrients_name}")
        st.write(f"{nutrients_manual}")
        new_df = s_df[s_df['成分名'].str.contains(n_select)]
        new_df_list = split_5(new_df)
        st.markdown("")
        st.markdown(f" ### {n_select}の成分を含むサプリはこちらです")
        st.write(f"**{len(new_df)}**件のサプリメント")
        num=5
        lcol =[]
        for b in range(len(new_df_list)):
            lcol.append(st.columns(num))
            m_list = new_df_list[b]['商品名'].unique().tolist()
            for a in range(num):
                with lcol[b][a]:
                    st.caption(m_list[a])
                    st.image(f"image/{m_list[a]}/{m_list[a]}_1.png")
                    st.link_button("詳細",f"https://www.diet-cafe.jp/search_result.html?cx=partner-pub-6658419875952282%3A2007643100&q={m_list[a]}")
    except:
        None

# データの取得
video_df = pd.read_csv("video_purpose_df_1.csv",encoding='UTF-8')
supple_df = pd.read_csv("supplement_purpose_df_1.csv",encoding='UTF-8')
supple_df = supple_df.sort_values('評価平均点', ascending=False)
nutrients_df = pd.read_csv("nutrients.csv",encoding='UTF-8')
nutrients_df =nutrients_df.drop(columns='Unnamed: 0')

# 運動目的2：運動目的の辞書作成
d_col = dict(zip(video_df['運動目的2'], video_df['運動目的']))

video_df_copy = video_df.copy()
st.title('運動動画検索とサプリメント推薦')
# st.markdown(" ## 検索")
# st.caption('テスト用')
# ボタン生成
home_btn = st.button('Home')

# 動的な変数を生成
if 'count' not in st.session_state:
    st.session_state['count'] = 0
if 'start_page' not in st.session_state:
    st.session_state['start_page'] = 1
if 'end_page' not in st.session_state:
    st.session_state['end_page'] = 10

# サイドバー作成に必要なリストの生成
video_purpose = video_df['運動目的2'].unique().tolist()
supple_id = supple_df['商品名'].unique().tolist()
nutrients_id = nutrients_df['栄養素'].unique().tolist()
video_purpose.insert(0,"--------")
supple_id.insert(0,"--------")
nutrients_id.insert(0,"--------")


#サイドバーの作成
st.sidebar.markdown("動画の検索")
name = st.sidebar.text_input("キーワード検索")
v_select = st.sidebar.selectbox("運動目的を選択してください", video_purpose)
st.sidebar.divider()
st.sidebar.markdown("サプリメントの検索")
n_btn = st.sidebar.button("栄養素一覧")
n_select = st.sidebar.selectbox("栄養素を選択してください", nutrients_id)
s_select = st.sidebar.selectbox("サプリメントを選択してください", supple_id)

# 検索結果のリセット
if home_btn:
    st.write(f"検索結果をリセットしました")
    st.session_state['count'] = 0
    st.session_state['start_page'] = 1
    st.session_state['end_page'] = 10
    name = ''
    v_select = "--------"
    s_select = "--------"
    
# ＆検索の実装
if name:
    result_df = video_df[video_df['title'].str.contains(name)]
    if v_select != "--------" :
        result_df = result_df[(result_df['運動目的2'] == v_select)]
        # supple_purpose = supplement_enter(supple_df,s_select)
elif v_select != "--------" :
    result_df = video_df[(video_df['運動目的2'] == v_select)]
elif s_select != "--------" :
    supple_purpose = supplement_enter(supple_df,s_select)
    result_df = video_df[video_df['運動目的'].str.contains(supple_purpose)]
else:
    result_df = pd.DataFrame(index=[])



if len(result_df) == 0:
    if n_btn:
        st.write(nutrients_df.drop(columns='運動目的'))
    elif n_select != "--------" :
        nutrients_supple_serch(n_select,supple_df,nutrients_df)
    else :
        st.write("検索結果はありません")
else:


    # サプリメントの推薦
    if v_select != "--------":
        supple_recommend(supple_df,d_col[v_select],v_select)

    if s_select !="--------":
        supple_only_recommend(s_select)


    select = st.selectbox('表示順',['視聴回数','高評価数','コメント数'])
    col2, col1 = st.columns(2)

    
    back_btn = col2.button('戻る')
    next_btn = col1.button('次へ')
    result_df = video_search_key(result_df,select)
    result_df_list = split_10(result_df)

    list_start = 0
    list_end = len(result_df_list)

    # if 'count' not in st.session_state:
    #     st.session_state['count'] = 0
    # if 'start_page' not in st.session_state:
    #     st.session_state['start_page'] = 1
    # if 'end_page' not in st.session_state:
    #     st.session_state['end_page'] = 10    

    if next_btn :
        st.session_state['count'] += 1
        st.session_state['start_page'] +=10
        st.session_state['end_page'] +=10
        # st.write(f"count：{st.session_state['count']}")
    if back_btn :
        if st.session_state['count'] != 0:
            st.session_state['count'] -= 1
            st.session_state['start_page'] -=10
            st.session_state['end_page'] -=10
        # st.write(f"count：{st.session_state['count']}")
    if st.session_state['count'] == list_end - 1:
        if name :
            st.write(
            f" **{name}** の検索結果 **{len(result_df)}** 件中 **{st.session_state['start_page']} - {len(result_df)}** 件目"
        )
        elif v_select != "--------" :
            st.write(
                f" **{v_select}** の検索結果 **{len(result_df)}** 件中 **{st.session_state['start_page']} - {len(result_df)}** 件目"
            )
        else :
            st.write(
                f" **{s_select}** の検索結果 **{len(result_df)}** 件中 **{st.session_state['start_page']} - {st.session_state['end_page']}** 件目"
            )
    else :
        if name :
            st.write(
            f" **{name}** の検索結果 **{len(result_df)}** 件中 **{st.session_state['start_page']} - {len(result_df)}** 件目"
        )
        elif v_select != "--------" :
            st.write(
                f" **{v_select}** の検索結果 **{len(result_df)}** 件中 **{st.session_state['start_page']} - {st.session_state['end_page']}** 件目"
            )
        else :
            st.write(
                f" **{s_select}** の検索結果 **{len(result_df)}** 件中 **{st.session_state['start_page']} - {st.session_state['end_page']}** 件目"
            )
    try:
        if name:
            search_name(result_df_list[st.session_state['count']],supple_df)
        elif v_select != "--------" :
            # df = video_search_key(result_df_list[st.session_state['count']],select)
            search(result_df_list[st.session_state['count']])
        else :
            # df = video_search_key(result_df_list[st.session_state['count']],select)
            search(result_df_list[st.session_state['count']])
    except:
        st.warning("戻るボタンを押してください")