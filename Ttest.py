import scipy.stats as stats

#Araştırma data'sı
questdata = [10, 10, 4, 3, 6, 4, 9, 5, 7, 6,
        6, 6, 9, 6, 8, 5, 8, 7, 8, 7,
        8, 10, 9, 7, 6, 4, 5, 4, 7, 9]

test_statistic, p_value = stats.ttest_1samp(questdata, popmean=5)

#tek yünlü p değerinin bölünmesi
p_value_one_tailed = p_value / 2

print(f"Örneklem ortalaması: {sum(questdata)/len(questdata):.2f}")
print(f"t değeri: {test_statistic:.4f}")
print(f"p-değeri (tek yönlü): {p_value_one_tailed:.4f}")

alpha = 0.05
if test_statistic > 0 and p_value_one_tailed < alpha:
    print("Sonuç: H0 reddedilir. Ortalama 5'ten anlamlı şekilde büyüktür.")
else:
    print("Sonuç: H0 reddedilemez. Ortalama 5'ten anlamlı şekilde büyük değildir.")
