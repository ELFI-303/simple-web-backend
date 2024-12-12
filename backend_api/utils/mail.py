from models.question import Question

def get_body(question: Question) -> str:
    return f"""
Bonjour,

Vous avez reçu un nouveau message de la part de {question.nom} le {question.date.strftime('%d/%m/%Y à %H:%M')}. Voici les détails :

Nom : {question.nom}
Adresse email : {question.email}
Message :
{question.message}

Cordialement,
L'équipe imtransition"""

def get_html_body(question: Question) -> str:
    return f"""
<!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif;line-height: 1.6;color: #333;">
    <div style="background-color: #f4f4f4;padding: 10px;border-bottom: 2px solid #ddd;">
        <h2>Nouveau message de <span style="color: #007BFF;font-weight: bold;">{question.nom}</span></h2>
    </div>
    <div style="padding: 15px;">
        <p><strong>Nom :</strong> {question.nom}</p>
        <p><strong>Adresse email :</strong> {question.email}</p>
        <p><strong>Message :</strong></p>
        <p>{question.message}</p>
    </div>
    <div style="margin-top: 20px;font-size: 0.9em;color: #555;">
        <p>Cordialement,</p>
        <p>L'équipe <strong>imtransition</strong></p>
    </div>
</body>
</html>
"""