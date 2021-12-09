# Dragon Cave Datasheet Builder

## 개요(Summary)

Dragon Cave의 드래곤을 조금 더 쉽게 관리하기 위해, 교배 편의성을 높이기 위해 만든 프로그램입니다.
프로그램을 실행하고 본인 아이디를 입력하면 스크롤에서 드래곤 리스트를 불러와서 csv파일로 몇가지 정보와 함께 리스트업 해줍니다.
제공되는 정보 : ID, 이름, 품종, 태어난 날, 성별, 부모, 세대, 배우자(이 중 품종과 세대는 현재 제공되지 않습니다. 추가될 예정입니다.)
혈통관리를 위해 만드는 프로그램이기 때문에 알, 해츨링, 죽은 용, 언데드, 고자룡은 제외됩니다.
혹시 제외된 것들도 필요한 사람이 있다면, 수정하는 것도 고려하겠습니다.

This program was created to improve the breeding convenience and to manage Dragon Cave's dragons more easily.
Run the program and enter your ID to load the scroll's dragon list and save it as a csv file with some information.
Information provided: ID, Name, Breed, Born in, Gender, Parent, Generation, Spouse
*These breeds and spouses are not currently available. It will be added later.
Eggs, Hatchlings, dead dragons, undead, and non-gender dragons are excluded from the list as their main purpose is to manage bloodlines.
If there is someone who needs the excluded ones, I will consider modifying them.

##<span style="color:red">exe파일을 디코딩하지 마세요
##<span style="color:red">Do not try to decode the exe file

***

## 사용법(Description)
아마도 백신이 바이러스로 오진할 텐데, 예외처리 해주세요. 예외처리 방법은 "백신이름 예외"라고 검색하시면 나옵니다.(ex - "어베스트 예외", "알약 예외" 등...)
Perhaps the antivirus will detect this as a virus. Please handle the exception.
py랑 exe 둘 중에 하나만 받으시면 됩니다. 선택 기준은 아래를 참고해주세요.
Download either py or exe. Decide which one to download as follows:

###1. exe
>파이썬 인터프리터가 뭐예요?
>I don't know what a python interpreter is.
or
>내 컴퓨터에 파이썬 인터프리터가 설치되지 않았다.
>I don't have python interpreter installed on my device.
or
>드케 API키가 없다.
>I don't have the Dragon Cave API key.

###2. py
>나는 파이썬 인터프리터를 쓸 수 있고, API키를 가지고 있다.
>I can use the Python interpreter and have an API key.

###3. py (OS other than Windows)
>윈도우가 아닌 다른 OS를 사용한다(맥, 리눅스 등).
>I use an OS other than Windows.
반드시 DC API와 파이썬 인터프리터가 있어야 합니다.
API key and interpreter are required.

두 가지 선택지가 있는 이유는 exe파일이 py보다 압도적으로 무겁기 때문입니다.
The reason I'm giving you two choices is that the exe is much larger than the py.
***

##\-- Environment --
exe파일은 윈도우환경에서만 작동합니다.
윈도우 10 이외의 환경에서 되도록이면 사용하지 말아주세요. 다른 윈도우 버전은 테스트를 안해봤습니다.
윈도우 8도 되기는 하겠지만 정상 작동할지 확신할 수 없습니다.
The exe only works on Windows.
Also, if possible, use it only in a Windows 10 environment. Not tested with other Windows versions.
Windows 8 will probably work without problems. But I can't say for sure.

***

## Prerequisite 
직접 컴파일 할 때는 다음과 같은 패키지가 필요합니다:
If you are compiling yourself, you will need the packages:
* beautifulsoup4
* pandas
```
pip install beautifulsoup4
conda install -c anaconda beautifulsoup4
```
```
pip install pandas
conda install pandas
```
