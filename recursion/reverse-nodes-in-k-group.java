/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (k == 1) {
            return head;
        }
        ListNode curr = head;
        int count = 0;
        while (curr != null) {
            count++;
            curr = curr.next;
        }
        int times = count / k;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode groupPrev = dummy;
        curr = head;
        for (int i = 0; i < times; i++) {
            ListNode temp = curr;
            for (int t = 0; t < k; t++) {
                temp = temp.next;
            }
            ListNode rest = temp;
            ListNode prev = rest;
            ListNode groupStart = curr;
            for (int j = 0; j < k; j++) {
                ListNode currNext = curr.next;
                curr.next = prev;
                prev = curr;
                curr = currNext;
            }
            groupPrev.next = prev;
            groupStart.next = curr;
            groupPrev = groupStart;
        }
        return dummy.next;
    }
}