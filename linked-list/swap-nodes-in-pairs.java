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
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode curr = head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        while(curr != null && curr.next != null) {
            ListNode currNext = curr.next;
            ListNode rest = currNext.next;
            currNext.next = curr;
            prev.next = currNext;
            curr.next = rest;
            prev = curr;
            curr = rest;
        }
        return dummy.next;
    }
}