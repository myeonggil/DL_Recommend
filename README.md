# ImageMatching Recommend Service

## 목적
```text
온라인 쇼핑에 이용률이 점점 늘어나 많은 쇼핑몰들이 생기고 있습니다. 
하지만, 방대한 쇼핑몰로 원하는 스타일의 옷을 찾는데 많은 불편함이 따릅니다. 
그래서 쇼핑몰의 데이터를 수집하여 사용자는 단순히 이미지를 등록하여 
유사한 스타일을 추천한다는 목적으로 이미지추천 서비스를 개발하였습니다.
```

## 디렉토리 구조
- 📂 __DL\_Recommend__
   - 📂 __ImageMatching__
     - 📂 __ImageMatching__
       - 📂 __settings__
         - 📄 [\_\_init\_\_.py](ImageMatching/ImageMatching/settings/__init__.py)
         - 📂 __\_\_pycache\_\___
           - 📄 [\_\_init\_\_.cpython\-35.pyc](ImageMatching/ImageMatching/settings/__pycache__/__init__.cpython-35.pyc)
           - 📄 [common.cpython\-35.pyc](ImageMatching/ImageMatching/settings/__pycache__/common.cpython-35.pyc)
           - 📄 [dev.cpython\-35.pyc](ImageMatching/ImageMatching/settings/__pycache__/dev.cpython-35.pyc)
         - 📄 [common.py](ImageMatching/ImageMatching/settings/common.py)
         - 📄 [dev.py](ImageMatching/ImageMatching/settings/dev.py)
         - 📄 [prod.py](ImageMatching/ImageMatching/settings/prod.py)
       - 📂 __static__

    	 - 인스타그램 오픈 소스 사용
         - 📂 __bootstrap__
         .
         .
         .

       - 프로젝트에서 사용하는 url을 참조하는 url을 정의하고 기본 layout을 메인 웹페이지나 하위 페이지에서 import해서 사용
       - 📂 __templates__
         - 📄 [404.html](ImageMatching/ImageMatching/templates/404.html)
         - 📄 [500.html](ImageMatching/ImageMatching/templates/500.html)
         - 📄 [layout.html](ImageMatching/ImageMatching/templates/layout.html)
       - 📄 [urls.py](ImageMatching/ImageMatching/urls.py)
       - 📄 [wsgi.py](ImageMatching/ImageMatching/wsgi.py)

     - 홈페이지별 크롤링 코드
     - 📄 [\_alondon.py](ImageMatching/_alondon.py)
     - 📄 [\_apparel.py](ImageMatching/_apparel.py)
     - 📄 [\_dj2.py](ImageMatching/_dj2.py)
     - 📄 [\_everfree.py](ImageMatching/_everfree.py)
     - 📄 [\_hummingsuper.py](ImageMatching/_hummingsuper.py)
     - 📄 [\_rakun.py](ImageMatching/_rakun.py)
     - 📄 [\_tiag.py](ImageMatching/_tiag.py)
     - 📄 [\_vintage.py](ImageMatching/_vintage.py)
     - 📂 __accounts__
       - 📄 [admin.py](ImageMatching/accounts/admin.py)
       - 📄 [apps.py](ImageMatching/accounts/apps.py)
       - 📄 [forms.py](ImageMatching/accounts/forms.py)

       - mysql DB 마이그레이션으로 서비스에 필요한 테이블 구조 정의
       - 📂 __migrations__
         - 📄 [0001\_initial.py](ImageMatching/accounts/migrations/0001_initial.py)
         - 📄 [0002\_auto\_20170618\_1148.py](ImageMatching/accounts/migrations/0002_auto_20170618_1148.py)
         .
         .
         .
         - 📄 [0012\_auto\_20170701\_1146.py](ImageMatching/accounts/migrations/0012_auto_20170701_1146.py)
         - 📄 [0013\_auto\_20170703\_1105.py](ImageMatching/accounts/migrations/0013_auto_20170703_1105.py)
         - 📄 [\_\_init\_\_.py](ImageMatching/accounts/migrations/__init__.py)

       - 마이그레이션전 필요한 테이블, 필드를 정의 
       - 📄 [models.py](ImageMatching/accounts/models.py)
       - 📄 [my\_adapter.py](ImageMatching/accounts/my_adapter.py)

       - 실제 서비스에 사용하는 페이지 템플릿
       - 📂 __templates__
         - 📂 __accounts__
           - 📄 [account\_change.html](ImageMatching/accounts/templates/accounts/account_change.html)
           - 📄 [layout.html](ImageMatching/accounts/templates/accounts/layout.html)
           - 📄 [login.html](ImageMatching/accounts/templates/accounts/login.html)
           - 📄 [password\_change.html](ImageMatching/accounts/templates/accounts/password_change.html)
           - 📄 [profile.html](ImageMatching/accounts/templates/accounts/profile.html)
           - 📄 [signup.html](ImageMatching/accounts/templates/accounts/signup.html)

       - 직접적인 url경로와 페이지 뷰를 컨트롤
       - 📄 [urls.py](ImageMatching/accounts/urls.py)
       - 📄 [views.py](ImageMatching/accounts/views.py)
     - 📂 __crawler__
       - 📄 [info\_save.py](ImageMatching/crawler/info_save.py)

     - CNN 학습에 필요한 데이터를 list형태로 저장해서 다시 학습을 진행할 때 바로학습을 데이터를 로드하여 학습할 수 있도록 구성
     - 📂 __learning__
       - 📄 [cardigan\_score.npy](ImageMatching/learning/cardigan_score.npy)
       - 📄 [checkpoint](ImageMatching/learning/checkpoint)
       - 📄 [coat\_score.npy](ImageMatching/learning/coat_score.npy)
       - 📄 [each\_hy\_value.py](ImageMatching/learning/each_hy_value.py)
       - 📄 [google\_tensor.py](ImageMatching/learning/google_tensor.py)
       - 📄 [image\_matching.ckpt.data\-00000\-of\-00001](ImageMatching/learning/image_matching.ckpt.data-00000-of-00001)
       - 📄 [image\_matching.ckpt.index](ImageMatching/learning/image_matching.ckpt.index)
       - 📄 [image\_matching.ckpt.meta](ImageMatching/learning/image_matching.ckpt.meta)
       - 📄 [imagelearning.py](ImageMatching/learning/imagelearning.py)
       - 📄 [imagenet\_example.py](ImageMatching/learning/imagenet_example.py)
       - 📄 [inceptionv3\_retrain.py](ImageMatching/learning/inceptionv3_retrain.py)
       - 📄 [jacket\_score.npy](ImageMatching/learning/jacket_score.npy)
       - 📄 [jeans\_score.npy](ImageMatching/learning/jeans_score.npy)
       - 📄 [load\_tensor.py](ImageMatching/learning/load_tensor.py)
       - 📄 [mnist\_lecture.py](ImageMatching/learning/mnist_lecture.py)
       - 📄 [output\_graph.pb](ImageMatching/learning/output_graph.pb)
       - 📄 [output\_labels.txt](ImageMatching/learning/output_labels.txt)
       - 📄 [padding\_score.npy](ImageMatching/learning/padding_score.npy)
       - 📄 [retrain\_run\_interface.py](ImageMatching/learning/retrain_run_interface.py)
       - 📄 [shirts\_score.npy](ImageMatching/learning/shirts_score.npy)
       - 📄 [slacks\_score.npy](ImageMatching/learning/slacks_score.npy)
       - 📄 [sweathers\_score.npy](ImageMatching/learning/sweathers_score.npy)
       - 📄 [top\_score.npy](ImageMatching/learning/top_score.npy)
     - 📄 [manage.py](ImageMatching/manage.py)
     - 📂 __media__
       - 📄 [image\_path\_ad.py](ImageMatching/media/image_path_ad.py)

       - 📂 __post__
         - 📄 [AAkZykvr.jpg](ImageMatching/media/post/AAkZykvr.jpg)
         .
         .
         .
         - 📄 [lylZcsHE.jpg](ImageMatching/media/post/lylZcsHE.jpg)
         - 📂 __mg__
           - 📂 __50__
             - 📄 [0150020003082.jpg](ImageMatching/media/post/mg/50/0150020003082.jpg)
             .
             .
             .
             - 📄 [tiag86\_4520.jpg](ImageMatching/media/post/mg/50/tiag86_4520.jpg)
           - 📂 __51__
             - 📄 [0030030004953.jpg](ImageMatching/media/post/mg/51/0030030004953.jpg)
             .
             .
             .
             - 📄 [tiag86\_5436.jpg](ImageMatching/media/post/mg/51/tiag86_5436.jpg)
           - 📂 __52__
             - 📄 [0020010002802.jpg](ImageMatching/media/post/mg/52/0020010002802.jpg)
             .
             .
             .
             - 📄 [tiag86\_5087.jpg](ImageMatching/media/post/mg/52/tiag86_5087.jpg)
           - 📂 __53__
             - 📄 [0020010003232.jpg](ImageMatching/media/post/mg/53/0020010003232.jpg)
             .
             .
             .
             - 📄 [tiag86\_1526.jpg](ImageMatching/media/post/mg/53/tiag86_1526.jpg)
         - 📄 [qIbDyMTq.jpg](ImageMatching/media/post/qIbDyMTq.jpg)
         - 📄 [ulUbwMaa.jpg](ImageMatching/media/post/ulUbwMaa.jpg)
         - 📄 [zMTDnvQN.jpg](ImageMatching/media/post/zMTDnvQN.jpg)
         - 📄 [zYvLXpoC.jpeg](ImageMatching/media/post/zYvLXpoC.jpeg)
     - 📄 [my\_file.npy](ImageMatching/my_file.npy)
     - 📂 __post__
       - 📄 [admin.py](ImageMatching/post/admin.py)
       - 📄 [apps.py](ImageMatching/post/apps.py)
       - 📄 [forms.py](ImageMatching/post/forms.py)
       - 📂 __migrations__
         - 📄 [0001\_initial.py](ImageMatching/post/migrations/0001_initial.py)
         - 📄 [0002\_auto\_20170623\_1339.py](ImageMatching/post/migrations/0002_auto_20170623_1339.py)
         - 📄 [0003\_comment.py](ImageMatching/post/migrations/0003_comment.py)
         - 📄 [0004\_auto\_20170628\_2209.py](ImageMatching/post/migrations/0004_auto_20170628_2209.py)
         - 📄 [0005\_auto\_20170629\_1421.py](ImageMatching/post/migrations/0005_auto_20170629_1421.py)
         - 📄 [0006\_auto\_20170703\_1105.py](ImageMatching/post/migrations/0006_auto_20170703_1105.py)
         - 📄 [0007\_learning\_result.py](ImageMatching/post/migrations/0007_learning_result.py)
         - 📄 [0008\_link.py](ImageMatching/post/migrations/0008_link.py)
         - 📄 [0009\_link\_site.py](ImageMatching/post/migrations/0009_link_site.py)
         - 📄 [0010\_google\_result.py](ImageMatching/post/migrations/0010_google_result.py)
         - 📄 [0011\_photo\_labeling.py](ImageMatching/post/migrations/0011_photo_labeling.py)
         - 📄 [\_\_init\_\_.py](ImageMatching/post/migrations/__init__.py)
         - 📂 __\_\_pycache\_\___
           - 📄 [0001\_initial.cpython\-35.pyc](ImageMatching/post/migrations/__pycache__/0001_initial.cpython-35.pyc)
           - 📄 [0002\_auto\_20170623\_1339.cpython\-35.pyc](ImageMatching/post/migrations/__pycache__/0002_auto_20170623_1339.cpython-35.pyc)
           - 📄 [0003\_comment.cpython\-35.pyc](ImageMatching/post/migrations/__pycache__/0003_comment.cpython-35.pyc)
           - 📄 [0004\_auto\_20170628\_2209.cpython\-35.pyc](ImageMatching/post/migrations/__pycache__/0004_auto_20170628_2209.cpython-35.pyc)
           - 📄 [0005\_auto\_20170629\_1421.cpython\-35.pyc](ImageMatching/post/migrations/__pycache__/0005_auto_20170629_1421.cpython-35.pyc)
           - 📄 [0006\_auto\_20170703\_1105.cpython\-35.pyc](ImageMatching/post/migrations/__pycache__/0006_auto_20170703_1105.cpython-35.pyc)
           - 📄 [0007\_learning\_result.cpython\-35.pyc](ImageMatching/post/migrations/__pycache__/0007_learning_result.cpython-35.pyc)
           - 📄 [0008\_link.cpython\-35.pyc](ImageMatching/post/migrations/__pycache__/0008_link.cpython-35.pyc)
           - 📄 [0009\_link\_site.cpython\-35.pyc](ImageMatching/post/migrations/__pycache__/0009_link_site.cpython-35.pyc)
           - 📄 [0010\_google\_result.cpython\-35.pyc](ImageMatching/post/migrations/__pycache__/0010_google_result.cpython-35.pyc)
           - 📄 [0011\_photo\_labeling.cpython\-35.pyc](ImageMatching/post/migrations/__pycache__/0011_photo_labeling.cpython-35.pyc)
           - 📄 [\_\_init\_\_.cpython\-35.pyc](ImageMatching/post/migrations/__pycache__/__init__.cpython-35.pyc)
       - 📄 [models.py](ImageMatching/post/models.py)
       - 📂 __templates__
         - 📂 __post__
           - 📄 [comment\_more\_ajax.html](ImageMatching/post/templates/post/comment_more_ajax.html)
           - 📄 [comment\_new\_ajax.html](ImageMatching/post/templates/post/comment_new_ajax.html)
           - 📄 [follow\_list.html](ImageMatching/post/templates/post/follow_list.html)
           - 📄 [include\_account.html](ImageMatching/post/templates/post/include_account.html)
           - 📄 [layout.html](ImageMatching/post/templates/post/layout.html)
           - 📄 [my\_post\_list.html](ImageMatching/post/templates/post/my_post_list.html)
           - 📄 [my\_post\_list\_detail.html](ImageMatching/post/templates/post/my_post_list_detail.html)
           - 📄 [post\_edit.html](ImageMatching/post/templates/post/post_edit.html)
           - 📄 [post\_list.html](ImageMatching/post/templates/post/post_list.html)
           - 📄 [post\_list\_ajax.html](ImageMatching/post/templates/post/post_list_ajax.html)
           - 📄 [post\_new.html](ImageMatching/post/templates/post/post_new.html)
           - 📄 [script\_ajax.html](ImageMatching/post/templates/post/script_ajax.html)
       - 📂 __templatetags__
         - 📄 [\_\_init\_\_.py](ImageMatching/post/templatetags/__init__.py)
         - 📂 __\_\_pycache\_\___
           - 📄 [\_\_init\_\_.cpython\-35.pyc](ImageMatching/post/templatetags/__pycache__/__init__.cpython-35.pyc)
           - 📄 [post\_extras.cpython\-35.pyc](ImageMatching/post/templatetags/__pycache__/post_extras.cpython-35.pyc)
         - 📄 [post\_extras.py](ImageMatching/post/templatetags/post_extras.py)
       - 📄 [tests.py](ImageMatching/post/tests.py)
       - 📄 [urls.py](ImageMatching/post/urls.py)
       - 📄 [views.py](ImageMatching/post/views.py)
   - 📄 [README.md](README.md)
   - 📄 [requirements.txt](requirements.txt)


## 프로세스

## 결과물
