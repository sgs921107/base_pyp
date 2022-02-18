#!/usr/bin/env python
# -*- coding=utf8 -*-
'''
Description: file content
'''
from utils.encrypt import EncryptAES, EncryptRSA


class TestEncrypt(object):
    text = "123456"

    aes_key = "0123456789abcdef"
    aes_iv = aes_key[::-1]

    def test_aes_ecb(self):
        for pad_type in EncryptAES.pad_funcs:
            aes_ecb = EncryptAES.ecb_instance(self.aes_key, pad_type=pad_type)
            ciphertext = aes_ecb.encrypt(self.text)
            have = aes_ecb.decrypt(ciphertext)
            assert have == self.text, "want aes_ecb.decrypt(ciphertext) == %s, have %s" % (self.text, have)

    def test_aes_cbc(self):
        for pad_type in EncryptAES.pad_funcs:
            aes_cbc_encrypt = EncryptAES.cbc_instance(self.aes_key, self.aes_iv, pad_type=pad_type)
            aes_cbc_decrypt = EncryptAES.cbc_instance(self.aes_key, self.aes_iv, pad_type=pad_type)
            ciphertext = aes_cbc_encrypt.encrypt(self.text)
            have = aes_cbc_decrypt.decrypt(ciphertext)
            assert have == self.text, "want aes_cbc_decryt.decrypt(ciphertext) == %s, have %s" % (self.text, have)

    def test_rsa_from_key(self):
        rsa_public_key = """
            -----BEGIN PUBLIC KEY-----
            MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0MoRtanr25hqRbXwdjBg
            z3dwwWqKX2zTxeuRe2GheCaoEflc+vxcUCOJS5Dvybq0FT/DXEc0sLE+X8+YWMvu
            KDyfPviCyesTMcm6ieQ75lSipc8se6QAzgL85LVuc69aaKiM0Nzjj0is2D645+vW
            DwFPDxs355xlcXjVsx+riuPxDPZWc+4jlXCF8Wr2tHkujTPCTT6dveFApAtS/vhD
            dEsOBA45pK8tcut5lfAGfnnY2/QZ3TQT8+Fq7jYOCs4eph3CzBeZgBMfSNbtkdNV
            PCLopdUCJyQ6q3wnaogfCMY3eWZrbfwSf1OMXA8vYYgiUQwdSaUbMg5UQPGfKOHe
            0wIDAQAB
            -----END PUBLIC KEY-----
        """
        rsa_private_key = """
            -----BEGIN RSA PRIVATE KEY-----
            MIIEpAIBAAKCAQEA0MoRtanr25hqRbXwdjBgz3dwwWqKX2zTxeuRe2GheCaoEflc
            +vxcUCOJS5Dvybq0FT/DXEc0sLE+X8+YWMvuKDyfPviCyesTMcm6ieQ75lSipc8s
            e6QAzgL85LVuc69aaKiM0Nzjj0is2D645+vWDwFPDxs355xlcXjVsx+riuPxDPZW
            c+4jlXCF8Wr2tHkujTPCTT6dveFApAtS/vhDdEsOBA45pK8tcut5lfAGfnnY2/QZ
            3TQT8+Fq7jYOCs4eph3CzBeZgBMfSNbtkdNVPCLopdUCJyQ6q3wnaogfCMY3eWZr
            bfwSf1OMXA8vYYgiUQwdSaUbMg5UQPGfKOHe0wIDAQABAoIBAQDN4xWHoKI2j5vs
            VjdjNN2ieFO2R0tgQj6q41s44dOKWgROhSoNTiHx3LkczTXIJdZDRfdt3cG1o3Kw
            pFPE7IRTJUSbog/G8YqiBB1wsKHoxfkFrMBexCEPBZ9AITFj3r02i08g/1FfD/lx
            3JgWC1ewwEeny91bBbx7Iv8Ifeh5MfgLeUDApqjK0XUTzsM8smExfWFt/hQUUHqD
            p0xu/ZPHsobwvLyahQeXMFYDfgyPS31kQ1H05psepcsGWgazGQBkrZsEMryyopaK
            kMvtQw3of0HH8XO0/3Tyid4y0pvhgz7xtz/mb21PSbOaaVkJujZ+Bah5uxPd902g
            6sfdPOxRAoGBAPtJYd5ZDj6NG3ru9hsYa2kVitM8fDlq3BLCAGw4ocV3xoXTxdeh
            Z2qvaYg8/g6guPCPJZ2SqWoeKK+16vB5ghd3RRza5/8ky1Ot7dtp+YNX0O6As6r1
            bfIGWy8EU+rWeImUeooWrqN8U2rY2YXa8mNSyufsHdfMcidH73iGd9uNAoGBANS0
            oALoXvVCibJHyXdSGURxJTPiArTe8gLrL5ca2OK5VWgIuBGueKh30PUEKIO1gctD
            1+mU0Byutyn52hrMVCqfI9F0DQiTtRbviIqHr4BKtMMD9jQ05Gy3WvG92PEVnpcM
            wUhNnax+11WaQqY91eTMZ9xDaN2/O5YIPeQ2SNvfAoGBAK05hwf6KEGikIEMXgeL
            q+/C8/JuTcxfB9q+dgAkghBYYzg6JrZhA6OdzIgoU5LN5O+gHnQjeDo5FB8crxqb
            CL0YcUJU/Xz7ZlcHHWMWCPUsAlGH01NU4Tfofc9Jknfe5TUib97lh/oXaIHNfxYx
            OsqRdmKueFwdCcxeYIybVeC5AoGAHDAXqGr88omvz8V9qGdj29MWuApyi1+kOMjM
            FL1FEr6218OYCRfS+5htQ5sad2HdYn+KJHVJIxPwSArJYZXEbaWLTJ2RgJp6fCCg
            OqOCmYDM9a8XuJFt2A5waerbzg8sZh4VmyxWAd8JUFnSDU/SgbCo7uKsCf7muZo8
            AXtEKocCgYBKm3nl1+X1VLQcfi3tgzHO6iv4F1WIwSd0RhhbDD/qEJF455KIMxm2
            1IeHgZXVjle3ql97E3yHSnMjDMAg1Z/pJUvAQBKDdPEDSPim6yJgrWxHUoc6AX2t
            WbBJJua/qBhRwKIx8Aue8gNo18j9wbIrPmpsY3s82/eLiAOF1m4tRA==
            -----END RSA PRIVATE KEY-----
        """
        public_rsa = EncryptRSA.from_key(rsa_public_key)
        private_rsa = EncryptRSA.from_key(rsa_private_key)
        b64_ciphertext = public_rsa.b64_encrypt(self.text)
        b64_have = private_rsa.b64_decrypt(b64_ciphertext)
        assert b64_have == self.text, "want private_rsa.b64_decrypt(b64_ciphertext) == %s, have %s" % (self.text, b64_have)
        hex_ciphertext = public_rsa.hex_encrypt(self.text)
        hex_have = private_rsa.hex_decrypt(hex_ciphertext)
        assert hex_have == self.text, "want private_rsa.hex_decrypt(hex_ciphertext) == %s, have %s" % (self.text, hex_have)

    def test_rsa_from_construct(self):
        # modules = "00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81"
        # e = "10001"
        # pubkey_rsa = EncryptRSA.from_construct((int(modules, base=16), int(e, base=16)))
        public_rsa = EncryptRSA.from_construct((
            26357211458503634443072125765343182175366721595794953948114602524920957296416595286508006508303965554632907907746345403393543820511850139497435509009864856856823317134291765388178203516568783431190696689449174069019504663824632289041763903307979691808649283460865044039542800587339847440198824276515937097123919182771659370656001996008720898056329262363238670043317547524296760695166575245765260921037922225337158098162479154217255185565871765994518898689856830384007985755175523017825326198879734535877966062254077048974580984705461696095616387926259990886602112216848041148298142732306882531715367316585924800929491,
            65537
        ))
        private_rsa = EncryptRSA.from_construct((
            26357211458503634443072125765343182175366721595794953948114602524920957296416595286508006508303965554632907907746345403393543820511850139497435509009864856856823317134291765388178203516568783431190696689449174069019504663824632289041763903307979691808649283460865044039542800587339847440198824276515937097123919182771659370656001996008720898056329262363238670043317547524296760695166575245765260921037922225337158098162479154217255185565871765994518898689856830384007985755175523017825326198879734535877966062254077048974580984705461696095616387926259990886602112216848041148298142732306882531715367316585924800929491,
            65537,
            25990831861654574965561121194303500179520724931715591098934255501099253646615177487310472383625312082239136769245087783079957320969815937793326932958047000003495181242973276622005959693940433618019286269623912040289523603526720574814425958087515381583315815385841041489532524081929673019367520907184017438068714531454354211007122140396190596800502022444379218121604771297123261632589445381664809901702891663215004535788441650594999323053599126025956659686904328924866119037761542761987121541765646927337040045111606403051448597376097398386888188835227749035791790049284747326462608505922184686457314244810943072365649,
            176459486280612802888625389944525302077768387605361604439427251552499025154698327385143426178157253981100024440954527144196133354040989176046965767802277093791026455811995924364259545633416171963911686686655773556565576380343849323108577380438844697359954849128048119493884622491602706497580682742190891850637,
            149366928432452546057948418034517424902608930337594360401781082641714744393480576688435408270738713625086757812028442023009990921270848579634288538978871602522365120893898337351296831770516013824499189783381588035494646925103994792167216486242633074417063064189301271084764815280228641540118146513947505253343,
            105019695686879718958206991323451642710780182768342186378326129268207450494815243710829722535286507036404795897014053993154554161708988774975403613152969324293124278184238456680814145929343422078639440802043093505822431442293356757253489156719776150801603164697701529890471690670978179783340527202957110666488
        ))
        b64_ciphertext = public_rsa.b64_encrypt(self.text)
        b64_have = private_rsa.b64_decrypt(b64_ciphertext)
        assert b64_have == self.text, "want private_rsa.b64_decrypt(b64_ciphertext) == %s, have %s" % (self.text, b64_have)
        hex_ciphertext = public_rsa.hex_encrypt(self.text)
        hex_have = private_rsa.hex_decrypt(hex_ciphertext)
        assert hex_have == self.text, "want private_rsa.hex_decrypt(hex_ciphertext) == %s, have %s" % (self.text, hex_have)


if __name__ == '__main__':
    pass
