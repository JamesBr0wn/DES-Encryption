import config


class DES:
    def __init__(self, key):
        self.key = key
        self.sub_keys = self.key_generate(self.key)
        self.sub_keys_inv = self.key_inverse(self.sub_keys)

    def encrypt(self, data):
        m0 = self.ip_permutatuion(data)
        rl = self.t_Iteration(m0, self.sub_keys)
        c = self.ip_inverse_permutatuion(rl)
        return c

    def decrypt(self, data):
        c0 = self.ip_permutatuion(data)
        rl = self.t_Iteration(c0, self.sub_keys_inv)
        c = self.ip_inverse_permutatuion(rl)
        return c

    def t_Iteration(self, data, sub_keys):
        l = []
        r = []
        for i in range(32):
            l.append(data[i])
            r.append(data[i+32])
        for i in range(16):
            l_next = r
            r = self.data_xor(l, self.feistel_substitution(r, sub_keys[i]))
            l = l_next
        res = []
        for i in range(32):
            res.append(r[i])
        for i in range(32):
            res.append(l[i])
        return res

    def feistel_substitution(self, data, key):
        ext_data = self.extend_permutatuion(data)
        ext_data = self.data_xor(ext_data, key)
        f_s = []
        for i in range(8):
            row = ext_data[6 * i] * 2 + ext_data[6 * i + 5]
            col = ext_data[6 * i + 1] * 8 + ext_data[6 * i + 2] * 4 + ext_data[6 * i + 3] * 2 + ext_data[6 * i + 4]
            temp_val = DESWrapper.data_to_bits(config.S_Box[i][row][col], 4)
            for j in range(4):
                f_s.append(temp_val[j])
        f_p = self.p_permutatuion(f_s)
        return f_p

    def ip_permutatuion(self, input_data):
        output_data = []
        for i in range(64):
            output_data.append(input_data[config.IP[i] - 1])
        return output_data

    def ip_inverse_permutatuion(self, input_data):
        output_data = []
        for i in range(64):
            output_data.append(input_data[config.IP_Reverse[i] - 1])
        return output_data

    def extend_permutatuion(self, input_data):
        output_data = []
        for i in range(48):
            output_data.append(input_data[config.Ext[i]-1])
        return output_data

    def p_permutatuion(self, input_data):
        output_data = []
        for i in range(32):
            output_data.append(input_data[config.P_Box[i]-1])
        return output_data

    def data_xor(self, left, right):
        result = []
        for i in range(len(left)):
            result.append(left[i] ^ right[i])
        return result

    def key_generate(self, key):
        key_56 = self.key_64_to_56(key)
        sub_key = []
        c = []
        d = []
        for i in range(28):
            c.append(key_56[i])
            d.append(key_56[i+28])
        for i in range(16):
            if i == 0 or i == 1 or i == 8 or i == 15:
                c = self.key_28_left_shift(c, 1)
                d = self.key_28_left_shift(d, 1)
            else:
                c = self.key_28_left_shift(c, 2)
                d = self.key_28_left_shift(d, 2)
            for j in range(28):
                key_56[j] = c[j]
                key_56[j+28] = d[j]
            sub_key.append(self.key_56_to_48(key_56))
        return sub_key

    def key_inverse(self, sub_keys):
        sub_keys_inv = [None for _ in range(16)]
        for i in range(16):
            sub_keys_inv[i] = sub_keys[15-i]
        return sub_keys_inv

    def key_64_to_56(self, key_64):
        key_56 = []
        for i in range(56):
            key_56.append(key_64[config.PC1[i]-1])
        return key_56

    def key_56_to_48(self, key_56):
        key_48 = []
        for i in range(48):
            key_48.append(key_56[config.PC2[i]-1])
        return key_48

    def key_28_left_shift(self, key_28, bit):
        key_28_shift = []
        for i in range(28):
            key_28_shift.append(key_28[(i + bit) % 28])
        return key_28_shift



class DESWrapper:
    def __init__(self, key):
        self.des = DES(DESWrapper.key_pre_processing(key))

    def encrypt(self, data):
        batch_data = DESWrapper.data_pre_processing(data)
        encrypted_data = []
        for i in range(len(batch_data)):
            encrypted_data.append(self.des.encrypt(batch_data[i]))
        encrypted_data = DESWrapper.data_post_processing(encrypted_data)
        return encrypted_data

    def decrypt(self, data):
        batch_data = DESWrapper.data_pre_processing(data)
        decrypted_data = []
        for i in range(len(batch_data)):
            decrypted_data.append(self.des.decrypt(batch_data[i]))
        decrypted_data = DESWrapper.data_post_processing(decrypted_data)
        return decrypted_data

    @staticmethod
    def data_to_bits(input_data, length):
        output_data = [0 for _ in range(8)]
        for i in range(length):
            if input_data == 0:
                break
            output_data[i] = input_data % 2
            input_data //= 2
        return output_data

    @staticmethod
    def batch_to_bits(input_data):
        output_data = []
        for ele in input_data:
            output_data = output_data + DESWrapper.data_to_bits(ele, 8)
        return output_data

    @staticmethod
    def data_pre_processing(data):
        data = list(data)
        if len(data) % 8 != 0:
            data = data[:] + [0 for _ in range(8 - len(data) % 8)]
        batch_num = len(data) // 8
        batch_data = []
        for i in range(batch_num):
            batch_data.append(DESWrapper.batch_to_bits(data[i * 8:(i + 1) * 8]))
        return batch_data

    @staticmethod
    def data_post_processing(batch_data):
        byte_stream = bytearray(len(batch_data) * len(batch_data[0]) // 8)
        for i in range(len(batch_data)):
            for j in range(len(batch_data[0]) // 8):
                char = 0
                weight = 1
                for k in range(8):
                    char += weight * batch_data[i][j * 8 + k]
                    weight *= 2
                byte_stream[i * len(batch_data[0]) // 8 + j] = char
        return byte_stream

    @staticmethod
    def key_pre_processing(key):
        key = bytes(key, encoding="utf-8")
        key = list(key)
        if len(key) < 8:
            key = key[:] + [0 for _ in range(8 - len(key))]
        elif len(key) > 8:
            key = key[:8]
        origin_key = DESWrapper.batch_to_bits(key)
        return origin_key


