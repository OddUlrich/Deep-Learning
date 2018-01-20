import tensorflow as tf 

lstm = tf.nn.run_cell.BasicLSTMCell(lstm_hidden_size)
# dropout_lstm = tf.nn.rnn_cell.DropoutWrapper(lstm, output_keep_prob=0.5)
# stacked_lstm = tf.nn.rnn_cell.MultiRNNCell([lstm] * number_of_layers)

state = lstm.zero_state(batch_size, tf.float32)

loss = 0.0
for i in range(num_steps):
	if i > 0:
		tf.get_variable_scope().reuse_variables()

	lstm_output, state = lstm(current_input, state)
	final_output = tf.nn.fully_connected(lstm_output)
	loss += tf.nn.calc_loss(final_output, expected_output)
