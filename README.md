# p4_meter
## meter

CIR（Committed Information Rate）：承诺信息速率，表示系统向 C桶中投放令牌的
速率，也就是说端口允许转发报文的平均速率； 
PIR（Peak Information Rate）：峰值信息速率，表示系统向P桶中投放令牌的速率，
也就是说端口应对突发流量时允许的最大转发速率，该值必须不小于CIR 的设置值； 
CBS（Committed Burst Size）：承诺突发大小，表示在部分流量未超过 CIR之前 C
桶瞬间能通过的突发流量，即C桶的容量，该值必须大于报文的最大长度； 
PBS（Peak Burst Size）：峰值突发大小，表示P桶的容量，用来定义端口瞬间能通
过的最大突发流量。
