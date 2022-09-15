import re


class Auth_checker:
    @classmethod
    def check_email(self, email):
        if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        return False
    @classmethod
    def check_pw(self, pw):
        result = re.fullmatch(r"^(?=.*[\d])(?=.*[a-z])(?=.*[0-9]){8,}$", pw)
        if result:
            return True
        return False
    @classmethod
    def check_job_status(self, job_status):
        if job_status in ['incumbent', 'take a leave of absence', 'job seeker', 'retiree']: # ['재직자', '휴직자', '취업준비생', '퇴직자']
            return True
        return False
    @classmethod
    def check_academic_status(self, academic_status):
        if academic_status in ['middle','high','undergraduate', 'graduate', 'doctoral degree']: # ['중학교', '고등학교', '대학교', '석사과정', '박사과정']
            return True
        return False
    @classmethod
    def check_specialization(self, specialization):
        if specialization in ["Humanities", "Social Sciences", "Arts and Physical Education", "Natural Sciences", 'Engineering', 'None']: # ['인문계열', '사회계열', '예체능계열', '자연계열', '공학계열', '선택안함']
            return True
        return False
    @classmethod
    def check_pre_startup(self, pre_startup):
        if pre_startup in [True, False]:
            return True
        return False
    @classmethod
    def signup_check(self, email, pw, job_status, academic_status, specialization, pre_startup):
        return self.check_email(email) and self.check_pw(pw) and self.check_job_status(job_status) and self.check_academic_status(academic_status) and self.check_specialization(specialization) and self.check_pre_startup(pre_startup)
