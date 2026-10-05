import cantools
import csv
import math
defextract_signal_info(dbc_filename, target_signal_name):
dbc_db = cantools.db.load_file(dbc_filename)

for message in dbc_db.messages:
for signal in message.signals:
if signal.name.lower() == target_signal_name.lower():
return signal.start, signal.length, signal.scale, signal.offset

return None, None, None, None
'''
defcalculate_row_number(start_bit, length):
total_bits = start_bit + length
    return total_bits // 8
'''
defcalculate_row_number(start_bit, length):
total_bits = (start_bit / 8)

return math.floor(total_bits)

defgenerate_c_code(signal_name, start_bit, length, factor, offset):
if length <1 or length >32:
print("Invalid length")
return
    if start_bit<0 or start_bit>= 500:
print("Invalid start bit")
return

row_number = calculate_row_number(start_bit, length)

shift_to_row_start = start_bit % 8
bitmask = (1 << length) - 1

if shift_to_row_start + length >8:  # two rows
lsb_part_length = 8 - shift_to_row_start
msb_part_length = length - lsb_part_length
msb_shift = lsb_part_length
c_line = f"sgw_U.swg_in.=(((((RxMsg.data8[{row_number}] >>{shift_to_row_start}) & 0X{((1 <<lsb_part_length) - 1):X}) + ((uint16_t)(RxMsg.data8[{row_number + 1}]  <<{msb_shift}) & 0X{((1 <<msb_part_length) - 1) <<lsb_part_length:X}))"

elifshift_to_row_start == 0:  # one row
c_line = f"sgw_U.swg_in.=(RxMsg.data8[{row_number}] & 0x{bitmask:X})"
else:
c_line = f"sgw_U.swg_in.=((RxMsg.data8[{row_number}] >>{shift_to_row_start}) & 0x{bitmask:X})"

# this condition is for signals that would exist in three rows
if (length >= 10 and length <= 17) and shift_to_row_start == 7:
lsb_part_length = 8 - shift_to_row_start
msb_part_length= length - lsb_part_length
msb_shift = lsb_part_length
second_part_shift= length - 8
third_part_shift = 8
first_row_mask = ((1 << (8 - shift_to_row_start)) - 1)
second_row_mask = ((1 <<8) - 1) <<lsb_part_length
third_row_mask = ((1 << (length - (8 + lsb_part_length))) - 1) <<third_part_shift + lsb_part_length
c_line = f"sgw_U.swg_in.=((((RxMsg.data8[{row_number}] >>{shift_to_row_start}) & 0X{first_row_mask:X}) + ((RxMsg.data8[{row_number + 1}] <<{msb_shift}) & 0X{second_row_mask:X}) + ((RxMsg.data8[{row_number + 2}] <<{msb_shift + third_part_shift}) & 0X{third_row_mask:X})"

elif(length >= 11 and length <= 18) and shift_to_row_start == 6:
lsb_part_length = 8 - shift_to_row_start
msb_part_length= length - lsb_part_length
msb_shift = lsb_part_length
second_part_shift= length - 8
third_part_shift = 8
first_row_mask = ((1 << (8 - shift_to_row_start)) - 1)
second_row_mask = ((1 <<8) - 1) <<lsb_part_length
third_row_mask = ((1 << (length - (8 + lsb_part_length))) - 1) <<third_part_shift + lsb_part_length
c_line = f"sgw_U.swg_in.=((((RxMsg.data8[{row_number}] >>{shift_to_row_start}) & 0X{first_row_mask:X}) + ((RxMsg.data8[{row_number + 1}] <<{msb_shift}) & 0X{second_row_mask:X}) + ((RxMsg.data8[{row_number + 2}] <<{msb_shift + third_part_shift}) & 0X{third_row_mask:X})"

elif(length >= 12 and length <= 19) and shift_to_row_start == 5:
lsb_part_length = 8 - shift_to_row_start
msb_part_length= length - lsb_part_length
msb_shift = lsb_part_length
second_part_shift= length - 8
third_part_shift = 8
first_row_mask = ((1 << (8 - shift_to_row_start)) - 1)
second_row_mask = ((1 <<8) - 1) <<lsb_part_length
third_row_mask = ((1 << (length - (8 + lsb_part_length))) - 1) <<third_part_shift + lsb_part_length
c_line = f"sgw_U.swg_in.=((((RxMsg.data8[{row_number}] >>{shift_to_row_start}) & 0X{first_row_mask:X}) + ((RxMsg.data8[{row_number + 1}] <<{msb_shift}) & 0X{second_row_mask:X}) + ((RxMsg.data8[{row_number + 2}] <<{msb_shift + third_part_shift}) & 0X{third_row_mask:X})"

elif(length >= 13 and length <= 20) and shift_to_row_start == 4:
lsb_part_length = 8 - shift_to_row_start
msb_part_length= length - lsb_part_length
msb_shift = lsb_part_length
second_part_shift= length - 8
third_part_shift = 8
first_row_mask = ((1 << (8 - shift_to_row_start)) - 1)
second_row_mask = ((1 <<8) - 1) <<lsb_part_length
third_row_mask = ((1 << (length - (8 + lsb_part_length))) - 1) <<third_part_shift + lsb_part_length
c_line = f"sgw_U.swg_in.=((((RxMsg.data8[{row_number}] >>{shift_to_row_start}) & 0X{first_row_mask:X}) + ((RxMsg.data8[{row_number + 1}] <<{msb_shift}) & 0X{second_row_mask:X}) + ((RxMsg.data8[{row_number + 2}] <<{msb_shift + third_part_shift}) & 0X{third_row_mask:X})"

elif(length >= 14 and length <= 21) and shift_to_row_start == 3:
lsb_part_length = 8 - shift_to_row_start
msb_part_length= length - lsb_part_length
msb_shift = lsb_part_length
second_part_shift= length - 8
third_part_shift = 8
first_row_mask = ((1 << (8 - shift_to_row_start)) - 1)
second_row_mask = ((1 <<8) - 1) <<lsb_part_length
third_row_mask = ((1 << (length - (8 + lsb_part_length))) - 1) <<third_part_shift + lsb_part_length
c_line = f"sgw_U.swg_in.=((((RxMsg.data8[{row_number}] >>{shift_to_row_start}) & 0X{first_row_mask:X}) + ((RxMsg.data8[{row_number + 1}] <<{msb_shift}) & 0X{second_row_mask:X}) + ((RxMsg.data8[{row_number + 2}] <<{msb_shift + third_part_shift}) & 0X{third_row_mask:X})"

elif(length >= 16 and length <= 22) and shift_to_row_start == 2:
lsb_part_length = 8 - shift_to_row_start
msb_part_length= length - lsb_part_length
msb_shift = lsb_part_length
second_part_shift= length - 8
third_part_shift = 8
first_row_mask = ((1 << (8 - shift_to_row_start)) - 1)
second_row_mask = ((1 <<8) - 1) <<lsb_part_length
third_row_mask = ((1 << (length - (8 + lsb_part_length))) - 1) <<third_part_shift + lsb_part_length
c_line = f"sgw_U.swg_in.=((((RxMsg.data8[{row_number}] >>{shift_to_row_start}) & 0X{first_row_mask:X}) + ((RxMsg.data8[{row_number + 1}] <<{msb_shift}) & 0X{second_row_mask:X}) + ((RxMsg.data8[{row_number + 2}] <<{msb_shift + third_part_shift}) & 0X{third_row_mask:X})"

elif(length >= 17 and length <= 23) and shift_to_row_start == 1:
lsb_part_length = 8 - shift_to_row_start
msb_part_length= length - lsb_part_length
msb_shift = lsb_part_length
second_part_shift= length - 8
third_part_shift = 8
first_row_mask = ((1 << (8 - shift_to_row_start)) - 1)
second_row_mask = ((1 <<8) - 1) <<lsb_part_length
third_row_mask = ((1 << (length - (8 + lsb_part_length))) - 1) <<third_part_shift + lsb_part_length
c_line = f"sgw_U.swg_in.=((((RxMsg.data8[{row_number}] >>{shift_to_row_start}) & 0X{first_row_mask:X}) + ((RxMsg.data8[{row_number + 1}] <<{msb_shift}) & 0X{second_row_mask:X}) + ((RxMsg.data8[{row_number + 2}] <<{msb_shift + third_part_shift}) & 0X{third_row_mask:X})"

elif(length >= 18 and length <= 24) and shift_to_row_start == 0:
lsb_part_length = 8 - shift_to_row_start
msb_part_length= length - lsb_part_length
msb_shift = lsb_part_length
second_part_shift= length - 8
third_part_shift = 8
first_row_mask = ((1 << (8 - shift_to_row_start)) - 1)
second_row_mask = ((1 <<8) - 1) <<lsb_part_length
third_row_mask = ((1 << (length - (8 + lsb_part_length))) - 1) <<third_part_shift + lsb_part_length
c_line = f"sgw_U.swg_in.=((((RxMsg.data8[{row_number}] >>{shift_to_row_start}) & 0X{first_row_mask:X}) + ((RxMsg.data8[{row_number + 1}] <<{msb_shift}) & 0X{second_row_mask:X}) + ((RxMsg.data8[{row_number + 2}] <<{msb_shift + third_part_shift}) & 0X{third_row_mask:X})"

if factor not in {0, 1}:
c_line = f"{c_line} * ({factor}))"

if offset != 0:
c_line += f" + ({offset}));"

# Initialize c_line_writing
c_line_writing = ""

# Check if the signal spans two rows
if shift_to_row_start>= 4 and (shift_to_row_start + length >8 and length <= 12):
msb_part_length = length - (8 - shift_to_row_start)
lsb_shift = shift_to_row_start
msb_shift= msb_part_length
msb_row_number = row_number + 1

c_line_writing += f"TxMsg.data8[{row_number}] = (TxMsg.data8[{row_number}] & 0x{((1 << (8 - lsb_shift)) - 1):X}) + ((sgw_Y.swg_out.<<{lsb_shift} )& 0x{((1 << (8 - lsb_shift)) - 1) ^ 0xFF:X})"
c_line_writing += f"\nTxMsg.data8[{msb_row_number}] =(TxMsg.data8[{msb_row_number}] & 0x{((1 << (msb_part_length)) - 1) ^ 0xFF:X})"
c_line_writing += f" + ((sgw_Y.swg_out. >>{(8 - lsb_shift)}) & 0X{((1 << (msb_part_length)) - 1):X})"

elifshift_to_row_start == 0 and (shift_to_row_start + length >8 and length <= 16):
msb_part_length = length - (8 - shift_to_row_start)
lsb_shift= shift_to_row_start
msb_shift= msb_part_length
msb_row_number = row_number + 1
first_row_length = (8 - shift_to_row_start)

c_line_writing += f"TxMsg.data8[{row_number}] = (TxMsg.data8[{row_number}] & 0x{((1 << (first_row_length)) - 1) ^ 0XFF:X}) + ((sgw_Y.swg_out.&0x{((1 << (8 - shift_to_row_start)) - 1) ^ 0X00:X})"
c_line_writing += f"\nTxMsg.data8[{msb_row_number}] =(TxMsg.data8[{msb_row_number}] & 0x{((1 << (msb_part_length)) - 1) ^ 0xFF:X})"
c_line_writing += f" + ((sgw_Y.swg_out. >>{8}) & 0X{((1 << (msb_part_length)) - 1):X})"

elifshift_to_row_start == 1 and (shift_to_row_start + length >8 and length <= 15):
msb_part_length = length - (8 - shift_to_row_start)
lsb_shift = shift_to_row_start
msb_shift= msb_part_length
msb_row_number = row_number + 1

c_line_writing += f"TxMsg.data8[{row_number}] = (TxMsg.data8[{row_number}] & 0X01) + ((sgw_Y.swg_out.<<{lsb_shift} )& 0XFE)"
c_line_writing += f"\nTxMsg.data8[{msb_row_number}] =(TxMsg.data8[{msb_row_number}] & 0x{((1 << (msb_part_length)) - 1) ^ 0xFF:X})"
c_line_writing += f" + ((sgw_Y.swg_out. >>{8 - shift_to_row_start}) & 0X{((1 << (msb_part_length)) - 1):X})"



elifshift_to_row_start == 2 and (shift_to_row_start + length >8 and shift_to_row_start + length <= 14):
msb_part_length = length - (8 - shift_to_row_start)
lsb_shift = shift_to_row_start
msb_shift= msb_part_length
msb_row_number = row_number + 1

c_line_writing += f"TxMsg.data8[{row_number}] = (TxMsg.data8[{row_number}] & 0X03) + ((sgw_Y.swg_out.<<{lsb_shift} )&0XFC)"
c_line_writing += f"\nTxMsg.data8[{msb_row_number}] =(TxMsg.data8[{msb_row_number}] & 0x{((1 << (msb_part_length)) - 1) ^ 0xFF:X})"
c_line_writing += f" + ((sgw_Y.swg_out. >>{8 - shift_to_row_start}) & 0X{((1 << (msb_part_length)) - 1):X})"


elifshift_to_row_start == 3 and (shift_to_row_start + length >8 and length <= 13):
msb_part_length = length - (8 - shift_to_row_start)
lsb_shift = shift_to_row_start
msb_shift= msb_part_length
msb_row_number = row_number + 1

c_line_writing += f"TxMsg.data8[{row_number}] = (TxMsg.data8[{row_number}] & 0X07) + ((sgw_Y.swg_out.<<{lsb_shift} )& 0XF8)"
c_line_writing += f"\nTxMsg.data8[{msb_row_number}] =(TxMsg.data8[{msb_row_number}] & 0x{((1 << (msb_part_length)) - 1) ^ 0xFF:X})"
c_line_writing += f" + ((sgw_Y.swg_out. >>{8 - shift_to_row_start}) & 0X{((1 << (msb_part_length)) - 1):X})"

# Signals spanning three rows
elif(shift_to_row_start>= 0 and shift_to_row_start<4) and (length >= 17 and length <= 24):
first_row_length = 8 - shift_to_row_start
second_row_length = 8
third_row_length = length - (second_row_length + first_row_length)
msb_part_length = length - (8 - shift_to_row_start)
lsb_shift = shift_to_row_start
msb_shift= msb_part_length
msb_row_number= row_number + 1

c_line_writing += f"TxMsg.data8[{row_number}] = (TxMsg.data8[{row_number}] & 0x{((1 << (shift_to_row_start)) - 1):X}) + ((sgw_Y.swg_out.<<{shift_to_row_start}) &0x{((1 << (shift_to_row_start)) - 1) ^ 0XFF:X})"
c_line_writing += f"\nTxMsg.data8[{row_number + 1}] =((TxMsg.data8[{row_number + 1}] & 0x{((1 << (second_row_length)) - 1) ^ 0xFF:X}))"
c_line_writing += f" + ((sgw_Y.swg_out. >>{8 - lsb_shift}) &0X{((1 << (second_row_length)) - 1):X}))"
c_line_writing += f"\nTxMsg.data8[{row_number + 2}] = ((TxMsg.data8[{row_number + 2}] & 0x{((1 << (third_row_length)) - 1) ^ 0XFF:X}) + (sgw_Y.swg_out. >>{first_row_length + second_row_length}) & 0x{((1 << (third_row_length)) - 1) ^ 0X00:X}))"



elifshift_to_row_start == 4 and (length >= 13 and length <= 20):
first_row_length = 8 - shift_to_row_start
second_row_length = 8
third_row_length = length - (second_row_length + first_row_length)
msb_part_length = length - (8 - shift_to_row_start)
lsb_shift = shift_to_row_start
msb_shift= msb_part_length
msb_row_number= row_number + 1

c_line_writing += f"TxMsg.data8[{row_number}] = (TxMsg.data8[{row_number}] & 0x{((1 << (shift_to_row_start)) - 1):X}) + ((sgw_Y.swg_out.<<{shift_to_row_start}) &0x{((1 << (shift_to_row_start)) - 1) ^ 0XFF:X})"
c_line_writing += f"\nTxMsg.data8[{row_number + 1}] =((TxMsg.data8[{row_number + 1}] & 0x{((1 << (second_row_length)) - 1) ^ 0xFF:X}))"
c_line_writing += f" + ((sgw_Y.swg_out. >>{8 - lsb_shift}) &0X{((1 << (second_row_length)) - 1):X}))"
c_line_writing += f"\nTxMsg.data8[{row_number + 2}] = ((TxMsg.data8[{row_number + 2}] & 0x{((1 << (third_row_length)) - 1) ^ 0XFF:X}) + (sgw_Y.swg_out. >>{first_row_length + second_row_length}) & 0x{((1 << (third_row_length)) - 1) ^ 0X00:X}))"

elifshift_to_row_start == 6 and (length >= 11 and length <= 18):
first_row_length = 8 - shift_to_row_start
second_row_length = 8
third_row_length = length - (second_row_length + first_row_length)
msb_part_length = length - (8 - shift_to_row_start)
lsb_shift = shift_to_row_start
msb_shift= msb_part_length
msb_row_number= row_number + 1

c_line_writing += f"TxMsg.data8[{row_number}] = (TxMsg.data8[{row_number}] & 0x{((1 << (shift_to_row_start)) - 1):X}) + ((sgw_Y.swg_out.<<{shift_to_row_start}) &0x{((1 << (shift_to_row_start)) - 1) ^ 0XFF:X})"
c_line_writing += f"\nTxMsg.data8[{row_number + 1}] =((TxMsg.data8[{row_number + 1}] & 0x{((1 << (second_row_length)) - 1) ^ 0xFF:X}))"
c_line_writing += f" + ((sgw_Y.swg_out. >>{8 - lsb_shift}) &0X{((1 << (second_row_length)) - 1):X}))"
c_line_writing += f"\nTxMsg.data8[{row_number + 2}] = ((TxMsg.data8[{row_number + 2}] & 0x{((1 << (third_row_length)) - 1) ^ 0XFF:X}) + (sgw_Y.swg_out. >>{first_row_length + second_row_length}) & 0x{((1 << (third_row_length)) - 1) ^ 0X00:X}))"


elifshift_to_row_start == 7 and (length >= 10 and length <= 17):
first_row_length = 8 - shift_to_row_start
second_row_length = 8
third_row_length = length - (second_row_length + first_row_length)
msb_part_length = length - (8 - shift_to_row_start)
lsb_shift = shift_to_row_start
msb_shift= msb_part_length
msb_row_number= row_number + 1

c_line_writing += f"TxMsg.data8[{row_number}] = (TxMsg.data8[{row_number}] & 0x{((1 << (shift_to_row_start)) - 1):X}) + ((sgw_Y.swg_out.<<{shift_to_row_start}) &0x{((1 << (shift_to_row_start)) - 1) ^ 0XFF:X})"
c_line_writing += f"\nTxMsg.data8[{row_number + 1}] =(TxMsg.data8[{row_number + 1}] & 0x{((1 << (second_row_length)) - 1) ^ 0xFF:X})"
c_line_writing += f" + ((sgw_Y.swg_out. >>{8 - lsb_shift}) &0X{((1 << (second_row_length)) - 1):X})"
c_line_writing += f"\nTxMsg.data8[{row_number + 2}] = ((TxMsg.data8[{row_number + 2}] & 0x{((1 << (third_row_length)) - 1) ^ 0XFF:X}) + ((sgw_Y.swg_out. >>{first_row_length + second_row_length}) &0x{((1 << (third_row_length)) - 1) ^ 0X00:X})"

elifshift_to_row_start == 0 and shift_to_row_start + length <= 8:
c_line_writing = f"TxMsg.data8[{row_number}] = (TxMsg.data8[{row_number}] & 0X{bitmask <<shift_to_row_start ^ 0XFF:X}) + (sgw_Y.swg_out. &0X{bitmask <<shift_to_row_start:X});"

else:
# Signal fits in one row
c_line_writing = f"TxMsg.data8[{row_number}] = (TxMsg.data8[{row_number}] & 0X{bitmask <<shift_to_row_start ^ 0XFF:X}) + ((sgw_Y.swg_out. <<{shift_to_row_start}) & 0X{bitmask <<shift_to_row_start:X});"

return c_line, c_line_writing
defmain():
csv_filename = input("Enter CSV file name: ")
dbc_filenames = input("Enter DBC file names separated by commas: ").split(',')

#read message name and corresponding signal names from the CSV file
with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
next(reader)  # skip header row of the CSV file
for column in reader:
message_name = column[3] # change here the column number where message name exists#################################
signal_names = [signal.strip() for signal in column[4].split(',')] # change here the column number where signals exist###################################################
print(f"Message '{message_name}' and Signal Names: {signal_names}")

found_signals = False
            for dbc_filenamein dbc_filenames:
dbc_db= cantools.db.load_file(dbc_filename)
for signal_namein signal_names:
start_bit, length, factor, offset = extract_signal_info(dbc_filename, signal_name)

if start_bitis None or length is None:
print(f"Signal '{signal_name}' not found in the DBC file '{dbc_filename}'.")
continue

print(f"Signal '{signal_name}': Start Bit - {start_bit}, Length - {length}, Factor - {factor}, Offset - {offset}")

# generate C code for the signal
reading_part, writing_part = generate_c_code(signal_name, start_bit, length, factor, offset)

# write the reading part to the output file
output_file = f"{dbc_filename}_{message_name}_signals.txt"
with open(output_file, 'a') as f:
f.write(f"Reading part for Signal '{signal_name}':\n{reading_part}\n\n")

if writing_part:
# write the writing part to the output file
with open(output_file, 'a') as f:
f.write(f"Writing part for Signal '{signal_name}':\n{writing_part}\n\n")

found_signals = True

                if found_signals:
break  # signals found, stop searching in other DBC files

    #process debug DBC file if available
debug_dbc_filename = input("Enter the name of the debug DBC file (if available): ")
if debug_dbc_filename:
dbc_db = cantools.db.load_file(debug_dbc_filename)
message_name = input("Enter the message name to process: ")
for message in dbc_db.messages:
if message.name == message_name:
print(f"Message '{message_name}' found in '{debug_dbc_filename}'.")
for signal in message.signals:
start_bit, length, factor, offset = signal.start, signal.length, signal.scale, signal.offset
print(f"Signal '{signal.name}': Start Bit - {start_bit}, Length - {length}, Factor - {factor}, Offset - {offset}")

# generate C code for the signal
reading_part, writing_part = generate_c_code(signal.name, start_bit, length, factor, offset)

# write the reading part to the output file
output_file = f"{debug_dbc_filename}_{message_name}_signals.txt"
with open(output_file, 'a') as f:
f.write(f"Reading part for Signal '{signal.name}':\n{reading_part}\n\n")

if writing_part:
# write the writing part to the output file
with open(output_file, 'a') as f:
f.write(f"Writing part for Signal '{signal.name}':\n{writing_part}\n\n")

if __name__ == "__main__":
    main()

