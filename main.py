def emphasis(signal_batch, emph_coeff=0.95, pre=True):
    """
    """
    result = np.zeros(signal_batch.shape)    # Форма голосового сигнала batch_sized заполнена 0
    for sample_idx, sample in enumerate(signal_batch): Функция #enumerate (), которая отображает данные и индексы данных одновременно
        for ch, channel_data in enumerate(sample):# Формула предыскажения y (n) = x (n) -ax (n-1)
            if pre:
                result[sample_idx][ch] = np.append(channel_data[0], channel_data[1:] - emph_coeff * channel_data[:-1])  
            else:
                result[sample_idx][ch] = np.append(channel_data[0], channel_data[1:] + emph_coeff * channel_data[:-1])
    return result
