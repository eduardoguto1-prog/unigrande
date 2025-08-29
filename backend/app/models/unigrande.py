from tortoise import fields, models
from tortoise.validators import MinValueValidator, MaxValueValidator


class PeriodoLetivo(models.Model):
    id = fields.IntField(pk=True)
    ano = fields.IntField() # ano que pode ser 2020, 2025
    semestre = fields.IntField() # semestre que pode ser 1 ou 2
    data_inicio = fields.DateField()
    data_fim = fields.DateField()

    class Meta:
        table = "periodos_letivos"
        unique_together = (("ano", "semestre"),)
        indexes = (("ano", "semestre"),)

class Professor(models.Model):
    id: int = fields.IntField(pk=True) # cria uma chave primária (pk)
    idt_prof: int = fields.IntField(validators=[MaxValueValidator(999999)]) # identificação do professor com o maximo de 6 digitos
    mat_prof: int = fields.IntField(validators=[MaxValueValidator(999999)]) # matricula do professor com o maximo de 6 digitos
    nom_prof: str = fields.CharField(max_length=50) # recebe o nome do professor com o maximo de 50 digitos

    class Meta:
        table = "professor" # cria uma tabela com o nome professor
        unique_together = (("idt_prof","mat_prof","nom_prof"),) # garante que a combinação de campos seja única na tabela , criando uma tupla
        indexes = (("idt_prof","mat_prof","nom_prof"),) # cria atalho para fazer uma busca mas rapido, melhorando o desempenho.


class Curso(models.Model):
    id: int = fields.IntField(pk=True) # cria uma chave primária (pk)
    cod_curso: int = fields.IntField() # recebe o codigo do curso
    nom_curso: str = fields.CharField(max_length=40) # recebe o nome do curso, com um maximo de 40 caracteres
    tot_cred: int = fields.IntField(validators=[MaxValueValidator(99)]) # recebe o total de credito
    idt_prof: int = fields.IntFiled(validators=[MaxValueValidator(999999)]) # recebe a identificação do professor

    class Meta:
        table = "curso" 
        unique_togather = (("cod_curso", "nom_curso", "tot_cred", "idt_prof"),)
        indexes = (("cod_curso", "nom_curso", "tot_cred", "idt_prof"),)

class Disciplina(models.Model):
    id: int = fields.IntField(pk=True)
    cod_disc: int = fields.IntField(validators=[MaxValueValidator(999999)]) # recebe o codigo da disciplina com o maximo de 6 digitos de 1 a 9
    nom_disc: str = fields.CharField(max_length=50) # recebe o nome da disciplina com um maximo de 50 caracteres
    creditos: int = fields.IntFiled(validators=[MaxValueValidator(99)]) # recebe creditos de 2 digitos
    top_disc: str = fields.CharFiled(max_length=9) # recebe o tipo de disciplina
    horas_obrig: int = fields.IntFiled(validators=[MaxValueValidator(99)]) # recebe as horas obrigatorias com 2 digitos
    limite_faltas: int = fields.IntField(validators[MaxValueValidator(99)]) # recebe o limite de faltas maximo de 2 digitos

    class Meta:
        table = "disciplina" 
        unique_togather = (("cod_disc", "nom_disc", "creditos", "top_disc", "horas_obrig", "limite_faltas"),)
        indexes = (("cod_disc", "nom_disc", "creditos", "top_disc", "horas_obrig", "limite_faltas"),)

class Matriz(models.Model):
    id: int = fields.IntFiled(pk=True)
    cod_disc: int = fields.IntField(validators=[MaxValueValidator(999999)]) # recebe o codigo da disciplina com o maximo de 6 digitos podendo ser de 1 a 9
    cod_curso: int = fields.IntField() # recebe o código do curso
    periodo: int = fields.IntField(validators=[MaxValueValidator(99)]) # recebe o periodo

    class Meta:
        table = "matriz"
        unique_togather = (("cod_disc", "cod_curso", "periodo"),)
        indexes = (("cod_disc", "cod_curso", "periodo"),)

class Turma(models.Model):
    id: int = fields.IntField(pk=True)
    ano: int = fields.IntField(validators=[MaxValueValidator(9999)]) # recebe o ano 
    semestre: int = fields.IntField(validators=[MaxValueValidator(99)]) # recebe a identificação do semestre
    cod_disc: int = fields.IntField(validators=[MaxValueValidator(999999)]) # recebe o codigo da disciplina
    vagas: int = fields.IntField(validators=[MaxValueValidator(999)]) # recebe vagas
    idt_prof: int = fields.IntField(validators=[MaxValueValidator(999999)]) # recebe a identificação do professor

    class Meta:
        table = "turma"
        unique_togather = (("ano", "semestre", "cod_disc", "vagas", "idt_prof"),)
        indexes = (("ano", "semestre", "cod_disc", "vagas", "idt_prof"),)

class Aluno(models.Model):
    pass

class Matricula(models.Model):
    pass

class Historico(models.Model):
    pass