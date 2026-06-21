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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int count = 0;
        ListNode curr = head;
        while (curr != null) {
            count++;
            curr = curr.next;
        }
        int pos = count - n + 1;
        if (pos == 1) {
            return head.next;
        }
        count = 1;
        curr = head;
        while (curr != null) {
            if (count == pos - 1) {
                curr.next = curr.next.next;
            }
            curr = curr.next;
            count++;
        }
        return head;
    }
}