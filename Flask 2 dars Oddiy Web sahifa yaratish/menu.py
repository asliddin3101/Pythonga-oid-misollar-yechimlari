from flask import Flask,render_template
from datetime import datetime

app=Flask(__name__)

@app.route("/")
def Home():
    title="АS нашрининг хабар беришича, «Барселона» «Ливерпул»га           яримҳимоячи Филиппе Коутиньони бепул қайтаришни таклиф қилган.Nega?"
    content="""
    Манбанинг хабарига кўра, бу ҳолатда каталонияликлар бразилияликнинг трансфери учун ҳали ҳам қарздор бўлган мерсисайдликларга қўшимча 50 миллион евро тўламайдилар. Бу ҳолат Филиппенинг олаётган катта маошининг ортиқчалиги билан ўлчанмоқда.
    Эслатиб ўтамиз, 2018 йилда «Барселона» Коутиньони «Ливерпул»дан 165 миллион еврога сотиб олганди. Ўтган мавсумда 28 ёшли бразилиялик яримҳимоячи Испания чемпионатида 12 ўйин ўтказиб, иккита гол урди ва шунча голга узатма берди.
    """
    date=datetime.now()
    views=156987
    return render_template("index.html",title=title,content=content,views=views,date=date)

app.run(debug=True)